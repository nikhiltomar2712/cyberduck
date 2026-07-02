"""Local secret-pattern detection for defensive reviews."""

from __future__ import annotations

import re

PATTERNS = {
    "generic_secret": re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[^'\"\s]{8,}"),
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "aws_access_key_id": re.compile(r"AKIA[0-9A-Z]{16}"),
}


def find_potential_secrets(text: str) -> list[str]:
    found: list[str] = []
    for name, pattern in PATTERNS.items():
        if pattern.search(text):
            found.append(name)
    return found
