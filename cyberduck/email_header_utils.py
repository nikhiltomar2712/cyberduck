"""Email header parsing helpers for phishing awareness."""

from __future__ import annotations

from email.parser import Parser


def parse_headers(raw_headers: str) -> dict[str, str]:
    message = Parser().parsestr(raw_headers)
    return {key.lower(): value for key, value in message.items()}


def authentication_results(headers: dict[str, str]) -> dict[str, bool]:
    combined = " ".join(value.lower() for key, value in headers.items() if key.lower() == "authentication-results")
    return {
        "spf_pass": "spf=pass" in combined,
        "dkim_pass": "dkim=pass" in combined,
        "dmarc_pass": "dmarc=pass" in combined,
    }
