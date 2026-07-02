"""Small semantic-version helpers."""

from __future__ import annotations

import re

SEMVER_PATTERN = re.compile(r"^(\d+)\.(\d+)\.(\d+)")


def parse_semver(version: str) -> tuple[int, int, int]:
    match = SEMVER_PATTERN.match(version.strip())
    if not match:
        raise ValueError(f"not a semantic version: {version}")
    return tuple(int(part) for part in match.groups())


def compare_versions(left: str, right: str) -> int:
    a = parse_semver(left)
    b = parse_semver(right)
    return (a > b) - (a < b)
