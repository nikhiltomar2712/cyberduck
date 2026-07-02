"""Offline password policy scoring."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass

from .constants import WEAK_PASSWORD_WORDS


@dataclass(frozen=True)
class PasswordReview:
    score: int
    label: str
    entropy_bits: float
    findings: tuple[str, ...]


def estimate_entropy_bits(password: str) -> float:
    """Estimate password entropy from character set size and length."""

    alphabet = 0
    alphabet += 26 if re.search(r"[a-z]", password) else 0
    alphabet += 26 if re.search(r"[A-Z]", password) else 0
    alphabet += 10 if re.search(r"\d", password) else 0
    alphabet += 33 if re.search(r"[^A-Za-z0-9]", password) else 0
    if not password or alphabet == 0:
        return 0.0
    return round(len(password) * math.log2(alphabet), 2)


def evaluate_password(password: str) -> PasswordReview:
    """Return a simple offline password review."""

    findings: list[str] = []
    score = 0
    if len(password) >= 16:
        score += 4
    elif len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 1
    else:
        findings.append("Use at least 12 characters; 16+ is better.")

    for pattern, label in [(r"[a-z]", "lowercase"), (r"[A-Z]", "uppercase"), (r"\d", "number"), (r"[^A-Za-z0-9]", "symbol")]:
        if re.search(pattern, password):
            score += 1
        else:
            findings.append(f"Add a {label} character.")

    lowered = password.lower()
    if lowered in WEAK_PASSWORD_WORDS or lowered.endswith("123"):
        score -= 3
        findings.append("Avoid common words and simple suffixes.")
    if re.search(r"(.)\1{2,}", password):
        score -= 1
        findings.append("Avoid repeated characters.")

    score = max(0, min(score, 10))
    label = "strong" if score >= 8 else "reasonable" if score >= 6 else "weak" if score >= 3 else "very weak"
    if not findings:
        findings.append("Good baseline. Keep it unique and store it in a password manager.")
    return PasswordReview(score, label, estimate_entropy_bits(password), tuple(findings))
