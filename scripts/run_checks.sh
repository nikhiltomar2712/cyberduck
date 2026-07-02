#!/usr/bin/env bash
set -euo pipefail

python -m compileall -q cyberduck tests tools
python -m unittest discover -q
python tools/password_strength_checker.py 'CorrectHorseBatteryStaple!42' >/dev/null
python tools/file_hash.py README.md >/dev/null
python tools/log_failed_login_summary.py examples/sample-auth.txt >/dev/null

echo "All local Cyberduck checks passed."
