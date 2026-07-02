"""Create local file inventories for defensive baselines."""

from __future__ import annotations

from pathlib import Path

from .hash_utils import hash_file


def inventory_directory(root: Path, pattern: str = "*") -> list[dict[str, str | int]]:
    items: list[dict[str, str | int]] = []
    for path in sorted(root.rglob(pattern)):
        if not path.is_file():
            continue
        items.append({"path": str(path.relative_to(root)), "size": path.stat().st_size, "sha256": hash_file(path)})
    return items
