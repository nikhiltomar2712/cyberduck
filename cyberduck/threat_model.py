"""STRIDE threat modeling prompts."""

from __future__ import annotations

STRIDE = {
    "spoofing": "Can someone pretend to be another user or service?",
    "tampering": "Can data be modified without permission?",
    "repudiation": "Could actions be denied because logs are weak?",
    "information disclosure": "Can private data leak?",
    "denial of service": "Can availability be disrupted?",
    "elevation of privilege": "Can someone gain more access than intended?",
}


def stride_questions() -> list[str]:
    return [f"{name.title()}: {question}" for name, question in STRIDE.items()]


def threat_summary(component: str, threats: list[str]) -> str:
    joined = ", ".join(threats) if threats else "no threats recorded"
    return f"{component}: {joined}"
