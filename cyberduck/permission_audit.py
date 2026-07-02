"""Permission helpers for local file reviews."""

from __future__ import annotations

import stat
from pathlib import Path


def mode_summary(path: Path) -> str:
    return stat.filemode(path.stat().st_mode)


def is_world_writable(path: Path) -> bool:
    return bool(path.stat().st_mode & stat.S_IWOTH)


def private_file_recommendation(path: Path) -> str:
    return "Restrict to owner read/write with chmod 600." if is_world_writable(path) else "No world-write bit detected."
