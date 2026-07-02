"""Hashing helpers for integrity practice."""

from __future__ import annotations

import hashlib
import hmac
from pathlib import Path


def hash_bytes(data: bytes, algorithm: str = "sha256") -> str:
    digest = hashlib.new(algorithm)
    digest.update(data)
    return digest.hexdigest()


def hash_text(text: str, algorithm: str = "sha256") -> str:
    return hash_bytes(text.encode("utf-8"), algorithm)


def hash_file(path: Path, algorithm: str = "sha256") -> str:
    digest = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def hashes_match(left: str, right: str) -> bool:
    return hmac.compare_digest(left.lower(), right.lower())
