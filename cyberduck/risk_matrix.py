"""Likelihood x impact risk scoring."""

from __future__ import annotations

from .models import RiskItem


def clamp_level(value: int) -> int:
    return max(1, min(int(value), 5))


def risk_score(likelihood: int, impact: int) -> int:
    return clamp_level(likelihood) * clamp_level(impact)


def risk_label(score: int) -> str:
    if score >= 20:
        return "critical"
    if score >= 12:
        return "high"
    if score >= 6:
        return "medium"
    return "low"


def sort_risks(items: list[RiskItem]) -> list[RiskItem]:
    return sorted(items, key=lambda item: item.score, reverse=True)
