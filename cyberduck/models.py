"""Small data models used by Cyberduck helpers."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Finding:
    """A single defensive review finding."""

    title: str
    severity: str = "info"
    detail: str = ""
    recommendation: str = ""


@dataclass(frozen=True)
class RiskItem:
    """Risk with normalized likelihood and impact values."""

    name: str
    likelihood: int
    impact: int
    notes: str = ""
    tags: tuple[str, ...] = field(default_factory=tuple)

    @property
    def score(self) -> int:
        return self.likelihood * self.impact
