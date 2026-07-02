"""Incident timeline helpers."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class TimelineEvent:
    when: datetime
    title: str
    detail: str = ""


def sort_events(events: list[TimelineEvent]) -> list[TimelineEvent]:
    return sorted(events, key=lambda event: event.when)


def render_timeline(events: list[TimelineEvent]) -> str:
    return "\n".join(f"- {event.when.isoformat()} — {event.title}" for event in sort_events(events))
