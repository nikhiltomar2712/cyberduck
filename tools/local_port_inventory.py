#!/usr/bin/env python3
"""List local listening ports using system tools.

This is a defensive inventory helper for your own machine. It does not scan
remote hosts.
"""

from __future__ import annotations

import shutil
import subprocess


def run(command: list[str]) -> int:
    print(f"$ {' '.join(command)}")
    completed = subprocess.run(command, text=True, check=False)  # noqa: S603
    return completed.returncode


def main() -> int:
    if shutil.which("ss"):
        return run(["ss", "-tulpen"])
    if shutil.which("netstat"):
        return run(["netstat", "-tulpen"])
    print("Neither ss nor netstat was found.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
