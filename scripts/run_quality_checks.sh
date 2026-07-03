#!/usr/bin/env bash
set -euo pipefail

echo "[quality] Running unit tests (Python)..."
python -m pytest -q

echo "[quality] Running shell lint (optional if shellcheck exists)..."
if command -v shellcheck >/dev/null 2>&1; then
  shellcheck scripts/*.sh || true
fi

echo "[quality] Running markdown link checks (optional)..."
if command -v mdformat >/dev/null 2>&1; then
  echo "mdformat present; skipping link check (customize as needed)."
fi

echo "[quality] Basic file structure validation..."
for d in docs checklists labs templates learning-paths resources tools; do
  if [[ ! -d "${d}" ]]; then
    echo "Missing directory: ${d}" >&2
    exit 1
  fi
done

echo "[quality] Done."

