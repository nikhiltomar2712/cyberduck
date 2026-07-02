"""Known-port explanations for local inventories."""

from __future__ import annotations

from .constants import COMMON_PORTS, RISKY_PUBLIC_PORTS


def describe_port(port: int) -> str:
    return COMMON_PORTS.get(port, "Unassigned or application-specific")


def is_risky_public_port(port: int) -> bool:
    return port in RISKY_PUBLIC_PORTS


def summarize_ports(ports: list[int]) -> list[str]:
    return [f"{port}: {describe_port(port)}" for port in sorted(set(ports))]
