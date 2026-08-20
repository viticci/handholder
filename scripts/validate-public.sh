#!/usr/bin/env bash
set -euo pipefail

skill_dir="$(cd "$(dirname "$0")/.." && pwd)"
failed=0

check() {
  label="$1"
  pattern="$2"
  if grep -RInE --exclude-dir='.git' --exclude='validate-public.sh' "$pattern" "$skill_dir"; then
    echo "validation failed: $label" >&2
    failed=1
  fi
}

check "unfinished scaffold text" '\[TODO|TODO:'
check "absolute macOS user path" '/Users/[^/$ ]+'
check "absolute Linux home path" '/home/[^/$ ]+'
check "personal Google Drive path" 'CloudStorage/GoogleDrive-|My Drive/ROMs'
check "email address" '[[:alnum:]._%+-]+@[[:alnum:].-]+\.[[:alpha:]]{2,}'
check "specific ADB serial" '(^|[^[:alnum:]])[0-9a-f]{8,16}([^[:alnum:]]|$)'
check "stale skill name" 'android-handheld-setup'

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

echo "Public-skill validation passed: no scaffold markers or personal host/device identifiers found."
