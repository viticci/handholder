#!/usr/bin/env python3
"""Convert a staged Dolphin DDS texture tree to Android-safe PNG files."""

from __future__ import annotations

import argparse
import os
import struct
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from shutil import copy2

from PIL import Image

try:
    import texture2ddecoder
except ImportError:
    texture2ddecoder = None


BC7_DXGI_FORMATS = {98, 99}  # BC7_UNORM and BC7_UNORM_SRGB


class TruncatedTextureError(ValueError):
    """Raised when a DDS header declares pixels that are not in the file."""


def dds_format(data: bytes) -> tuple[str, int | None]:
    if len(data) < 128 or data[:4] != b"DDS ":
        raise ValueError("not a valid DDS file")

    fourcc = data[84:88]
    if fourcc != b"DX10":
        return fourcc.decode("ascii", errors="replace").rstrip("\0"), None
    if len(data) < 148:
        raise ValueError("truncated DDS DX10 header")
    return "DX10", struct.unpack_from("<I", data, 128)[0]


def decode_dds(source: Path) -> tuple[Image.Image, str]:
    data = source.read_bytes()
    fourcc, dxgi = dds_format(data)

    if fourcc == "DX10" and dxgi in BC7_DXGI_FORMATS:
        if texture2ddecoder is None:
            raise RuntimeError(
                "BC7 DDS requires texture2ddecoder; install it in an isolated "
                "environment with: python3 -m pip install texture2ddecoder"
            )
        height = struct.unpack_from("<I", data, 12)[0]
        width = struct.unpack_from("<I", data, 16)[0]
        required_payload = ((width + 3) // 4) * ((height + 3) // 4) * 16
        actual_payload = len(data) - 148
        if actual_payload < required_payload:
            raise TruncatedTextureError(
                f"BC7 payload is truncated: expected at least {required_payload} "
                f"bytes, found {actual_payload}"
            )
        decoded = texture2ddecoder.decode_bc7(data[148:], width, height)
        image = Image.frombytes("RGBA", (width, height), decoded, "raw", "BGRA")
        return image, f"BC7-DXGI-{dxgi}"

    with Image.open(source) as opened:
        opened.load()
        return opened.copy(), fourcc if dxgi is None else f"DXGI-{dxgi}"


def convert(item: tuple[Path, Path]) -> tuple[str, str]:
    source, destination = item
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        image, decoder = decode_dds(source)
        image.save(destination, format="PNG", optimize=False, compress_level=6)
        stat = source.stat()
        os.utime(destination, (stat.st_atime, stat.st_mtime))
        return "ok", decoder
    except TruncatedTextureError as error:
        return "skipped", f"{source}: {error}"
    except Exception as error:
        return "error", f"{source}: {error}"


def is_metadata(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    return "__MACOSX" in relative.parts or any(part.startswith("._") for part in relative.parts)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    source = args.source.resolve()
    destination = args.destination.resolve()
    if source == destination or source in destination.parents:
        raise SystemExit("destination must not be the source or live inside it")
    if not source.is_dir():
        raise SystemExit(f"source directory does not exist: {source}")
    if args.workers < 1:
        raise SystemExit("--workers must be at least 1")

    files = sorted(
        path
        for path in source.rglob("*")
        if path.is_file() and path.suffix.lower() == ".dds" and not is_metadata(path, source)
    )
    jobs = [
        (path, destination / path.relative_to(source).with_suffix(".png"))
        for path in files
    ]

    errors: list[str] = []
    skipped: list[str] = []
    decoders: Counter[str] = Counter()
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        for status, detail in executor.map(convert, jobs):
            if status == "error":
                errors.append(detail)
            elif status == "skipped":
                skipped.append(detail)
            else:
                decoders[detail] += 1

    for path in source.rglob("*"):
        if not path.is_file() or path.suffix.lower() == ".dds" or is_metadata(path, source):
            continue
        target = destination / path.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        copy2(path, target)

    decoder_summary = ",".join(f"{name}:{count}" for name, count in sorted(decoders.items()))
    print(
        f"converted={sum(decoders.values())} skipped_invalid={len(skipped)} "
        f"errors={len(errors)} "
        f"decoders={decoder_summary or 'none'}"
    )
    for item in skipped:
        print(f"SKIPPED {item}")
    for error in errors:
        print(f"ERROR {error}")
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
