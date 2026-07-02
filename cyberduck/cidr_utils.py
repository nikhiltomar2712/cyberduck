"""CIDR helpers for local network notes."""

from __future__ import annotations

import ipaddress


def contains_ip(network: str, ip: str) -> bool:
    return ipaddress.ip_address(ip) in ipaddress.ip_network(network, strict=False)


def network_summary(network: str) -> dict[str, str | int]:
    net = ipaddress.ip_network(network, strict=False)
    return {
        "network": str(net.network_address),
        "broadcast": str(net.broadcast_address),
        "prefixlen": net.prefixlen,
        "num_addresses": net.num_addresses,
    }
