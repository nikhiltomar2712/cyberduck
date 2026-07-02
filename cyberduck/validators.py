"""Input validators for local defensive tools."""

from __future__ import annotations

import ipaddress
import re

DOMAIN_PATTERN = re.compile(r"^(?=.{1,253}$)([a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,63}$")


def is_ipv4(value: str) -> bool:
    """Return True when value is a valid IPv4 address."""

    try:
        return ipaddress.ip_address(value).version == 4
    except ValueError:
        return False


def is_domain_like(value: str) -> bool:
    """Return True for basic DNS-style host names."""

    return bool(DOMAIN_PATTERN.match(value.strip()))


def permission_reminder() -> str:
    """Standard permission reminder for security tooling."""

    return "Use only on systems you own or have explicit permission to assess."
