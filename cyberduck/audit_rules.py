"""Simple audit rule catalog."""

from __future__ import annotations

RULES = {
    "ACC-001": "Enable MFA on critical accounts.",
    "SYS-001": "Apply security updates regularly.",
    "WEB-001": "Enforce server-side authorization checks.",
    "LOG-001": "Preserve logs for incident investigations.",
    "SEC-001": "Do not commit secrets to source control.",
}


def get_rule(rule_id: str) -> str:
    return RULES[rule_id.upper()]


def search_rules(keyword: str) -> dict[str, str]:
    needle = keyword.lower()
    return {rule_id: text for rule_id, text in RULES.items() if needle in text.lower()}
