#!/usr/bin/env python3
"""Summarize failed login lines from an auth log or journal export."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

IP_PATTERN = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
FAIL_PATTERN = re.compile(r"failed|failure|invalid", re.IGNORECASE)


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize failed login attempts from a text log.")
    parser.add_argument("logfile", type=Path)
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()

    counters: Counter[str] = Counter()
    total = 0
    with args.logfile.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if not FAIL_PATTERN.search(line):
                continue
            total += 1
            for ip in IP_PATTERN.findall(line):
                counters[ip] += 1

    print(f"Failed-login-like lines: {total}")
    if counters:
        print("Top source IPs:")
        for ip, count in counters.most_common(args.top):
            print(f"- {ip}: {count}")
    else:
        print("No source IP addresses found in matching lines.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
