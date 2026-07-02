"""Tiny SBOM helpers for requirements-style files."""

from __future__ import annotations

import re

REQ_PATTERN = re.compile(r"^\s*([A-Za-z0-9_.-]+)\s*(?:==|>=|<=|~=|>|<)?\s*([^#;\s]+)?")


def parse_requirement_line(line: str) -> tuple[str, str | None] | None:
    clean = line.strip()
    if not clean or clean.startswith("#"):
        return None
    match = REQ_PATTERN.match(clean)
    if not match:
        return None
    return match.group(1).lower(), match.group(2)


def package_names(lines: list[str]) -> list[str]:
    names: list[str] = []
    for line in lines:
        parsed = parse_requirement_line(line)
        if parsed:
            names.append(parsed[0])
    return names
