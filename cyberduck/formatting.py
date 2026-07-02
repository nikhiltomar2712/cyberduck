"""Markdown formatting helpers."""

from __future__ import annotations


def bullet_list(items: list[str]) -> str:
    """Return a Markdown bullet list."""

    return "\n".join(f"- {item}" for item in items)


def checkbox(label: str, checked: bool = False) -> str:
    """Return a Markdown checkbox line."""

    mark = "x" if checked else " "
    return f"- [{mark}] {label}"


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    """Build a simple Markdown table."""

    header = "| " + " | ".join(headers) + " |"
    divider = "| " + " | ".join("---" for _ in headers) + " |"
    body = ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join([header, divider, *body])
