"""Pure validators for UDP GStreamer receiver CLI (offline-testable)."""

from __future__ import annotations


def validate_udp_port(port) -> int:
    """Return port if it is an int in 1..65535; else raise ValueError."""
    if isinstance(port, bool) or not isinstance(port, int):
        raise ValueError(f"port must be an int, got {type(port).__name__}")
    if port < 1 or port > 65535:
        raise ValueError(f"port must be in 1..65535, got {port}")
    return port


def validate_window_name(name) -> str:
    """Return non-empty stripped window name; else raise ValueError."""
    if not isinstance(name, str):
        raise ValueError(f"name must be a str, got {type(name).__name__}")
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must be a non-empty string")
    return cleaned
