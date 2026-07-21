"""Mission leaf action name allowlist (import-safe offline)."""

KNOWN_ACTIONS = frozenset({
    "takeoff",
    "land",
    "orbit",
    "wait",
    "offboard",
    "reposition",
    "speed",
    "check_blackboard",
})


def is_known_mission_action(action) -> bool:
    """Return True if action is a supported mission tree leaf name."""
    return isinstance(action, str) and action in KNOWN_ACTIONS
