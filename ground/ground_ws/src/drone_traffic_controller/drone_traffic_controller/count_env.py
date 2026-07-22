"""Parse non-negative integer drone-count environment variables safely."""

from __future__ import annotations
import os
import re

_NONNEG_INT = re.compile(r"^(0|[1-9][0-9]*)$")


def parse_nonneg_int_env(primary: str, *fallbacks: str, default: str = "0") -> int:
    """Read primary then fallbacks from the environment; require non-neg int text.

    Raises ValueError if the resolved raw value is not a non-negative integer
    written without sign or leading zeros (except plain \"0\").
    """
    raw = None
    for key in (primary, *fallbacks):
        if key in os.environ:
            raw = os.environ[key]
            break
    if raw is None:
        raw = default
    if not isinstance(raw, str) or not _NONNEG_INT.fullmatch(raw):
        keys = " / ".join((primary, *fallbacks))
        raise ValueError(f"{keys} must be a non-negative integer, got {raw!r}")
    return int(raw)
