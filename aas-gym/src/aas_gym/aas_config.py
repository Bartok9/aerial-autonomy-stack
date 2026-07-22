"""Pure AASEnv configuration validators (no Docker/ROS imports)."""

from __future__ import annotations
import math

ALLOWED_AUTOPILOTS = frozenset({"px4", "ardupilot"})
ALLOWED_ODOM = frozenset({"none", "openvins", "fastlio", "superodom", "mimosa"})
ALLOWED_RENDER_MODES = frozenset({None, "human", "ansi"})


def validate_aas_config(
    *,
    instance: int = 0,
    gym_freq_hz: int = 50,
    autopilot: str = "px4",
    odom: str = "none",
    num_quads: int = 1,
    render_mode=None,
) -> dict:
    """Validate constructor knobs; raise ValueError on bad input.

    Returns a normalized dict of the checked fields.
    """
    if isinstance(instance, bool) or not isinstance(instance, int) or instance < 0:
        raise ValueError(f"instance must be a non-negative int, got {instance!r}")
    if isinstance(gym_freq_hz, bool) or not isinstance(gym_freq_hz, int) or gym_freq_hz < 1:
        raise ValueError(f"gym_freq_hz must be an int >= 1, got {gym_freq_hz!r}")
    if autopilot not in ALLOWED_AUTOPILOTS:
        raise ValueError(f"autopilot must be one of {sorted(ALLOWED_AUTOPILOTS)}, got {autopilot!r}")
    if odom not in ALLOWED_ODOM:
        raise ValueError(f"odom must be one of {sorted(ALLOWED_ODOM)}, got {odom!r}")
    if isinstance(num_quads, bool) or not isinstance(num_quads, int) or num_quads < 1:
        raise ValueError(f"num_quads must be an int >= 1, got {num_quads!r}")
    if render_mode not in ALLOWED_RENDER_MODES:
        raise ValueError(f"render_mode must be one of human/ansi/None, got {render_mode!r}")
    return {
        "instance": instance,
        "gym_freq_hz": gym_freq_hz,
        "autopilot": autopilot,
        "odom": odom,
        "num_quads": num_quads,
        "render_mode": render_mode,
    }


def validate_zmq_transport(transport: str) -> str:
    if transport not in ("tcp", "ipc"):
        raise ValueError(f"ZMQ_TRANSPORT must be 'tcp' or 'ipc', got {transport!r}")
    return transport


def finite_episode_seconds(value) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"seconds must be numeric, got {type(value).__name__}")
    f = float(value)
    if not math.isfinite(f) or f <= 0:
        raise ValueError(f"seconds must be finite and > 0, got {f!r}")
    return f
