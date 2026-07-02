"""Cryptography policy helpers for checklists."""

from __future__ import annotations

from .constants import WEAK_HASHES


def weak_hash_algorithm(name: str) -> bool:
    return name.strip().lower().replace("-", "") in {item.replace("-", "") for item in WEAK_HASHES}


def is_tls_version_acceptable(version: str) -> bool:
    normalized = version.strip().lower().replace(" ", "")
    return normalized in {"tls1.2", "tls1.3"}


def crypto_recommendation(topic: str) -> str:
    topic = topic.lower()
    if topic in {"md5", "sha1"}:
        return "Use SHA-256 or better for integrity checks."
    if topic in {"tls1.0", "tls1.1"}:
        return "Disable old TLS versions; prefer TLS 1.2 or 1.3."
    return "Use maintained libraries and modern defaults."
