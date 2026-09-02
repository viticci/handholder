#!/usr/bin/env bash
set -euo pipefail

skill_dir="$(cd "$(dirname "$0")/.." && pwd)"
failed=0

check() {
  label="$1"
  pattern="$2"
  if grep -RInE --exclude-dir='.git' --exclude='validate-public.sh' --exclude='*.png' "$pattern" "$skill_dir"; then
    echo "validation failed: $label" >&2
    failed=1
  fi
}

check "unfinished scaffold text" '\[TODO|TODO:'
check "absolute macOS user path" '/Users/[^/$ ]+'
check "absolute Linux home path" '/home/[^/$ ]+'
check "absolute Windows user path" '[A-Za-z]:\\Users\\[^\\ ]+'
check "absolute mounted-volume path" '/Volumes/[^/$ ]+'
check "personal Google Drive path" 'CloudStorage/GoogleDrive-|My Drive/ROMs'
check "email address" '[[:alnum:]._%+-]+@[[:alnum:].-]+\.[[:alpha:]]{2,}'
check "specific ADB serial" '(^|[^[:alnum:]])[0-9a-f]{8,16}([^[:alnum:]]|$)'
check "probable long hex token" '(^|[^[:alnum:]])[0-9a-f]{24,64}([^[:alnum:]]|$)'
check "known secret prefix" '(^|[^[:alnum:]_])(AKIA[0-9A-Z]{16}|ghp_[[:alnum:]]{20,}|github_pat_[[:alnum:]_]{20,}|sk-[[:alnum:]_-]{20,}|eyJ[[:alnum:]_-]{20,}\.)'
check "private key material" 'BEGIN (OPENSSH|RSA|EC|DSA|PGP) PRIVATE KEY'
check "stale skill name" 'android-handheld-setup'

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

echo "Public-skill validation passed: no scaffold markers, likely secrets, or personal host/device identifiers found."
