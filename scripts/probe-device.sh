#!/usr/bin/env bash
set -euo pipefail

adb_bin="${ADB_BIN:-}"
if [[ -z "$adb_bin" ]]; then
  adb_bin="$(command -v adb || true)"
fi
if [[ -z "$adb_bin" || ! -x "$adb_bin" ]]; then
  echo "adb not found; install Android platform-tools or set ADB_BIN" >&2
  exit 1
fi

serial="${1:-${ANDROID_SERIAL:-}}"
if [[ -z "$serial" ]]; then
  candidates="$($adb_bin devices | awk 'NR > 1 && $2 == "device" {print $1}')"
  count="$(printf '%s\n' "$candidates" | awk 'NF {n++} END {print n+0}')"
  if [[ "$count" -ne 1 ]]; then
    echo "Expected one authorized ADB device, found $count; pass a serial explicitly" >&2
    "$adb_bin" devices -l >&2
    exit 2
  fi
  serial="$candidates"
fi

adb=("$adb_bin" -s "$serial")
state="$("${adb[@]}" get-state 2>/dev/null || true)"
if [[ "$state" != "device" ]]; then
  echo "ADB device is not authorized and online: $serial" >&2
  exit 3
fi

prop() {
  "${adb[@]}" shell getprop "$1" | tr -d '\r'
}

echo "== Identity =="
echo "adb: $adb_bin"
echo "serial: $serial"
echo "manufacturer: $(prop ro.product.manufacturer)"
echo "brand: $(prop ro.product.brand)"
echo "model: $(prop ro.product.model)"
echo "device: $(prop ro.product.device)"
echo "android: $(prop ro.build.version.release)"
echo "sdk: $(prop ro.build.version.sdk)"
echo "build: $(prop ro.build.display.id)"
echo "security_patch: $(prop ro.build.version.security_patch)"

echo
echo "== Storage =="
"${adb[@]}" shell 'df -h /storage/emulated/0 /storage/* 2>/dev/null | head -30'
"${adb[@]}" shell 'for root in /storage/emulated/0/ROMs /storage/*/ROMs; do if [ -d "$root" ]; then echo "ROM root: $root"; du -sh "$root" 2>/dev/null || true; fi; done'

echo
echo "== Displays =="
"${adb[@]}" shell dumpsys SurfaceFlinger --display-id 2>/dev/null || true
"${adb[@]}" shell dumpsys display 2>/dev/null | grep -E 'DisplayDeviceInfo|mDisplayId=|Display [0-9]+ info' | head -100 || true

echo
echo "== Focus =="
"${adb[@]}" shell dumpsys window 2>/dev/null | grep -E 'mCurrentFocus|mFocusedApp' | tail -12 || true

echo
echo "== Input devices =="
"${adb[@]}" shell dumpsys input 2>/dev/null | grep -A10 -B2 -E 'Controller|Gamepad|Path: /dev/input/event' | head -160 || true

echo
echo "== Relevant packages =="
"${adb[@]}" shell pm list packages 2>/dev/null | grep -Ei 'cocoon|retroarch|dolphin|ppsspp|aethersx|nethersx|armsx|mupen|flycast|azahar|melon|gamenative|emulationstation' | sort || true

echo
echo "Read-only probe complete. Verify displays, controls, and storage in the live UI before automation."
