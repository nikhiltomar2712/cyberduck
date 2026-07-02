"""Parser for security.txt style contact files."""

from __future__ import annotations


def parse_security_txt(text: str) -> dict[str, list[str]]:
    values: dict[str, list[str]] = {}
    for line in text.splitlines():
        clean = line.strip()
        if not clean or clean.startswith("#") or ":" not in clean:
            continue
        key, value = clean.split(":", 1)
        values.setdefault(key.strip().lower(), []).append(value.strip())
    return values


def has_contact(text: str) -> bool:
    return "contact" in parse_security_txt(text)
