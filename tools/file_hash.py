#!/usr/bin/env python3
"""Calculate file hashes for integrity checks."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def hash_file(path: Path, algorithm: str) -> str:
    digest = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate file hashes for verification.")
    parser.add_argument("files", nargs="+", type=Path, help="Files to hash")
    parser.add_argument("-a", "--algorithm", default="sha256", choices=hashlib.algorithms_guaranteed)
    args = parser.parse_args()

    for file_path in args.files:
        if not file_path.is_file():
            print(f"SKIP {file_path}: not a file")
            continue
        print(f"{args.algorithm}  {hash_file(file_path, args.algorithm)}  {file_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
