#!/usr/bin/env bash
# Builds a throwaway copilot repo filled with the sample company's sources.
# Usage: ./setup.sh [--seeded] [target-dir]   (default: /tmp/crewline-test)
#   --seeded  also fills the wiki with pages built from the sources, for testing
#             skills that start from a filled wiki.
# The target sits outside this repo so your agent loads only the test copy's AGENTS.md.
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
root="$(cd "$here/../.." && pwd)"
seeded=no
if [ "${1:-}" = "--seeded" ]; then
  seeded=yes
  shift
fi
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

if [ "$seeded" = yes ]; then
  cp -R "$here/seed/wiki/." "$target/wiki/"
  cat "$here/seed/log-entry.txt" >> "$target/wiki/log.md"
  # Add each seed index line under its heading in wiki/index.md.
  python3 - "$here/seed/index-entries.txt" "$target/wiki/index.md" <<'PY'
import sys
entries, index_path = sys.argv[1], sys.argv[2]
add, head = {}, None
for line in open(entries, encoding="utf-8").read().splitlines():
    if line.startswith("## "):
        head = line
    elif line.strip():
        add.setdefault(head, []).append(line)
out = []
for line in open(index_path, encoding="utf-8").read().splitlines():
    out.append(line)
    if line in add:
        out.append("")
        out.extend(add.pop(line))
if add:
    sys.exit("index heading not found: " + ", ".join(add))
open(index_path, "w", encoding="utf-8").write("\n".join(out) + "\n")
PY
fi

cd "$target"
git init -q -b main
git add -A
git -c user.name=sample -c user.email=sample@example.invalid commit -q \
  -m "Copilot with Tidewater Software sample sources"

echo "Ready: $target (seeded wiki: $seeded)"
echo "Next: cd \"$target\", start your agent there, and say for example:"
if [ "$seeded" = yes ]; then
  echo "  Did offline mode work?"
else
  echo "  Ingest every raw file the check script lists as not ingested, oldest first, without stopping."
fi
echo "Grade the run with the matching file in $here/expected/."
