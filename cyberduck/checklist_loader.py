"""Markdown checklist parsing helpers."""

from __future__ import annotations

import re

CHECKBOX_PATTERN = re.compile(r"^- \[( |x|X)\] (.+)$")


def parse_checkboxes(lines: list[str]) -> list[tuple[bool, str]]:
    boxes: list[tuple[bool, str]] = []
    for line in lines:
        match = CHECKBOX_PATTERN.match(line.strip())
        if match:
            boxes.append((match.group(1).lower() == "x", match.group(2)))
    return boxes


def completion_ratio(lines: list[str]) -> float:
    boxes = parse_checkboxes(lines)
    if not boxes:
        return 0.0
    return sum(1 for checked, _ in boxes if checked) / len(boxes)
