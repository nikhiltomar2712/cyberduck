#!/usr/bin/env python3
"""Offline password strength checker.

This tool does not send passwords anywhere. It estimates strength using length,
character variety, and common weak-pattern checks. Do not paste real production
passwords into shared terminals or recordings.
"""

from __future__ import annotations

import argparse
import getpass
import re
from dataclasses import dataclass

COMMON = {
    "password", "password1", "123456", "123456789", "qwerty", "admin",
    "letmein", "welcome", "iloveyou", "monkey", "dragon", "football",
}


@dataclass
class Result:
    score: int
    label: str
    findings: list[str]


def score_password(password: str) -> Result:
    findings: list[str] = []
    score = 0

    length = len(password)
    if length >= 16:
        score += 4
    elif length >= 12:
        score += 3
    elif length >= 8:
        score += 1
    else:
        findings.append("Use at least 12 characters; 16+ is better.")

    checks = [
        (r"[a-z]", "lowercase letters"),
        (r"[A-Z]", "uppercase letters"),
        (r"\d", "numbers"),
        (r"[^A-Za-z0-9]", "symbols"),
    ]
    variety = sum(bool(re.search(pattern, password)) for pattern, _ in checks)
    score += variety
    for pattern, name in checks:
        if not re.search(pattern, password):
            findings.append(f"Add {name}.")

    lowered = password.lower()
    if lowered in COMMON:
        score -= 4
        findings.append("This is a very common password.")
    if re.search(r"(.)\1{2,}", password):
        score -= 1
        findings.append("Avoid repeated characters.")
    if re.search(r"(?:1234|abcd|qwer|asdf)", lowered):
        score -= 1
        findings.append("Avoid keyboard or alphabet sequences.")

    score = max(0, min(score, 8))
    if score >= 7:
        label = "strong"
    elif score >= 5:
        label = "reasonable"
    elif score >= 3:
        label = "weak"
    else:
        label = "very weak"

    if not findings:
        findings.append("Good baseline. Prefer a unique passphrase stored in a password manager.")
    return Result(score=score, label=label, findings=findings)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check password strength offline.")
    parser.add_argument("password", nargs="?", help="Password to check. Omit to enter hidden input.")
    args = parser.parse_args()

    password = args.password if args.password is not None else getpass.getpass("Password: ")
    result = score_password(password)
    print(f"Strength: {result.label} ({result.score}/8)")
    for finding in result.findings:
        print(f"- {finding}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
