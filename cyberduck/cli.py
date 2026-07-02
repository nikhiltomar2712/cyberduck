"""Small command-line entry point for Cyberduck package helpers."""

from __future__ import annotations

import argparse

from .hash_utils import hash_text
from .password_policy import evaluate_password
from .risk_matrix import risk_label, risk_score


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Cyberduck defensive helper CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    password = sub.add_parser("password", help="Evaluate a sample password offline")
    password.add_argument("value")

    digest = sub.add_parser("hash-text", help="Hash text for integrity practice")
    digest.add_argument("value")
    digest.add_argument("--algorithm", default="sha256")

    risk = sub.add_parser("risk", help="Calculate likelihood x impact risk")
    risk.add_argument("likelihood", type=int)
    risk.add_argument("impact", type=int)

    args = parser.parse_args(argv)
    if args.command == "password":
        result = evaluate_password(args.value)
        print(f"{result.label}: {result.score}/10")
        for finding in result.findings:
            print(f"- {finding}")
        return 0
    if args.command == "hash-text":
        print(hash_text(args.value, args.algorithm))
        return 0
    if args.command == "risk":
        score = risk_score(args.likelihood, args.impact)
        print(f"{score}: {risk_label(score)}")
        return 0
    return 2
