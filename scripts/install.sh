#!/usr/bin/env bash
set -euo pipefail

DESTINATION="${1:-$HOME/.codex/skills/movie-companion}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [ -e "$DESTINATION" ]; then
  echo "Destination already exists: $DESTINATION" >&2
  exit 1
fi

mkdir -p "$(dirname "$DESTINATION")"
mkdir -p "$DESTINATION"

for item in SKILL.md agents references scripts examples README.md LICENSE; do
  if [ -e "$REPO_ROOT/$item" ]; then
    cp -R "$REPO_ROOT/$item" "$DESTINATION/$item"
  fi
done

echo "Installed movie-companion to $DESTINATION"
echo "Restart Codex to pick up new skills."
