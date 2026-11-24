#!/usr/bin/env bash
# Builds a throwaway copilot repo filled with the sample company's sources.
# Usage: ./setup.sh [target-dir]   (default: /tmp/crewline-test)
# The target sits outside this repo so your agent loads only the test copy's AGENTS.md.
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
root="$(cd "$here/../.." && pwd)"
target="${1:-/tmp/crewline-test}"

if [ -e "$target" ]; then
  echo "Target $target already exists. For a clean run, remove it with: rm -rf \"$target\"" >&2
  exit 1
fi
mkdir -p "$target"

# Copy the repo as git sees it: tracked files plus new files that aren't
# ignored. That leaves out your own raw/ files and the examples/ folder, so
# the copilot never sees the answer key or the checklists.
(
  cd "$root"
  git ls-files -co --exclude-standard | grep -v '^examples/' | tar -cf - -T -
) | tar -xf - -C "$target"

# The sample company's sources.
cp -R "$here/raw/." "$target/raw/"

cd "$target"
git init -q -b main
git add -A
git -c user.name=sample -c user.email=sample@example.invalid commit -q \
  -m "Copilot with Tidewater Software sample sources"

echo "Ready: $target"
echo "Next: cd \"$target\", start your agent there, and say for example:"
echo "  Ingest every raw file the check script lists as not ingested, oldest first, without stopping."
echo "Grade the run with the matching file in $here/expected/."
