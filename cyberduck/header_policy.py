"""HTTP security header policy checks."""

from __future__ import annotations

from .constants import RECOMMENDED_SECURITY_HEADERS


def normalize_headers(headers: dict[str, str]) -> dict[str, str]:
    return {key.lower(): value for key, value in headers.items()}


def missing_headers(headers: dict[str, str]) -> list[str]:
    normalized = normalize_headers(headers)
    return [header for header in RECOMMENDED_SECURITY_HEADERS if header not in normalized]


def grade_headers(headers: dict[str, str]) -> str:
    missing = len(missing_headers(headers))
    if missing == 0:
        return "A"
    if missing <= 1:
        return "B"
    if missing <= 3:
        return "C"
    return "D"
