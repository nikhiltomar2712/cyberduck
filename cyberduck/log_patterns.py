"""Defensive log parsing patterns."""

from __future__ import annotations

import re
from collections import Counter

IP_PATTERN = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
FAIL_PATTERN = re.compile(r"failed|failure|invalid", re.IGNORECASE)


def extract_ips(text: str) -> list[str]:
    return IP_PATTERN.findall(text)


def failed_login_lines(lines: list[str]) -> list[str]:
    return [line for line in lines if FAIL_PATTERN.search(line)]


def count_failed_login_ips(lines: list[str]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for line in failed_login_lines(lines):
        counter.update(extract_ips(line))
    return counter
