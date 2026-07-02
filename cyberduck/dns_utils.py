"""DNS text parsing helpers."""

from __future__ import annotations


def normalize_record_name(name: str) -> str:
    return name.strip().rstrip(".").lower()


def parse_hosts_lines(lines: list[str]) -> dict[str, str]:
    records: dict[str, str] = {}
    for line in lines:
        clean = line.split("#", 1)[0].strip()
        if not clean:
            continue
        parts = clean.split()
        if len(parts) < 2:
            continue
        ip, *names = parts
        for name in names:
            records[normalize_record_name(name)] = ip
    return records
