#!/usr/bin/env python3
"""Build a screen-appropriate edition of a Dolphin PNG texture pack."""

from __future__ import annotations

import argparse
import os
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from shutil import copy2

from PIL import Image


TEXTURE_SIZE = re.compile(r"^tex1_(\d+)x(\d+)_")
MIP_LEVEL = re.compile(r"_mip(\d+)(?:\.|$)")


def expected_size(path: Path, scale: int) -> tuple[int, int] | None:
    match = TEXTURE_SIZE.match(path.name)
    if not match:
        return None
    width, height = map(int, match.groups())
    mip_match = MIP_LEVEL.search(path.name)
    mip = int(mip_match.group(1)) if mip_match else 0
    divisor = 1 << mip
    native_width = max(1, width // divisor)
    native_height = max(1, height // divisor)
    return native_width * scale, native_height * scale


def resize(item: tuple[Path, Path, int]) -> tuple[str, str]:
    source, destination, scale = item
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        target = expected_size(source, scale)
        with Image.open(source) as opened:
            opened.load()
            image = opened.copy()

        if target is None or (image.width <= target[0] and image.height <= target[1]):
            copy2(source, destination)
            return "copied", str(source)

        source_ratio = image.width / image.height
        target_ratio = target[0] / target[1]
        if abs(source_ratio - target_ratio) / target_ratio <= 0.01:
            output_size = target
        else:
            factor = min(target[0] / image.width, target[1] / image.height)
            output_size = (
                max(1, round(image.width * factor)),
                max(1, round(image.height * factor)),
            )

        image.resize(output_size, Image.Resampling.LANCZOS).save(
            destination, format="PNG", optimize=False, compress_level=6
        )
        stat = source.stat()
        os.utime(destination, (stat.st_atime, stat.st_mtime))
        return "resized", f"{source}: {image.size} -> {output_size}"
    except Exception as error:
        return "error", f"{source}: {error}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--scale", type=int, default=2)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    source = args.source.resolve()
    destination = args.destination.resolve()
    if source == destination or source in destination.parents:
        raise SystemExit("destination must not be the source or live inside it")
    if not source.is_dir():
        raise SystemExit(f"source directory does not exist: {source}")
    if args.scale < 1 or args.workers < 1:
        raise SystemExit("--scale and --workers must be at least 1")

    png_files = sorted(path for path in source.rglob("*.png") if path.is_file())
    jobs = [
        (path, destination / path.relative_to(source), args.scale)
        for path in png_files
    ]
    counts = {"resized": 0, "copied": 0, "error": 0}
    errors: list[str] = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        for status, detail in executor.map(resize, jobs):
            counts[status] += 1
            if status == "error":
                errors.append(detail)

    for path in source.rglob("*"):
        if not path.is_file() or path.suffix.lower() == ".png":
            continue
        target = destination / path.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        copy2(path, target)

    print(
        f"resized={counts['resized']} copied={counts['copied']} "
        f"errors={counts['error']} scale={args.scale}x"
    )
    for error in errors:
        print(error)
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
