"""MFA recommendation helpers."""

from __future__ import annotations

STRENGTH_ORDER = ["none", "sms", "totp", "push", "hardware_key", "passkey"]


def mfa_strength(method: str) -> int:
    normalized = method.strip().lower().replace("-", "_")
    return STRENGTH_ORDER.index(normalized) if normalized in STRENGTH_ORDER else 0


def best_mfa_method(methods: list[str]) -> str:
    if not methods:
        return "none"
    return max(methods, key=mfa_strength)


def recommend_upgrade(current: str) -> str:
    if mfa_strength(current) < mfa_strength("totp"):
        return "Use at least an authenticator app; hardware keys or passkeys are better."
    return "Good baseline. Prefer phishing-resistant hardware keys or passkeys for critical accounts."
