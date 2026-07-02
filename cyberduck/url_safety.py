"""URL safety heuristics for awareness training."""

from __future__ import annotations

import ipaddress
from urllib.parse import urlparse


def normalize_url(url: str) -> str:
    if "://" not in url:
        return "https://" + url
    return url


def is_https_url(url: str) -> bool:
    return urlparse(normalize_url(url)).scheme == "https"


def suspicious_url_reasons(url: str) -> list[str]:
    parsed = urlparse(normalize_url(url))
    reasons: list[str] = []
    if parsed.scheme != "https":
        reasons.append("not_https")
    host = parsed.hostname or ""
    try:
        ipaddress.ip_address(host)
        reasons.append("ip_address_host")
    except ValueError:
        pass
    if "@" in parsed.netloc:
        reasons.append("userinfo_in_url")
    if len(host.split(".")) > 4:
        reasons.append("many_subdomains")
    return reasons
