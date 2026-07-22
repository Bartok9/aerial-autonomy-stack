"""Offline-testable bounds checks for YOLO CLI (camera-id, hfov)."""

from __future__ import annotations
import math


def validate_camera_id(camera_id) -> int:
    if isinstance(camera_id, bool) or not isinstance(camera_id, int):
        raise ValueError(f"camera_id must be int, got {type(camera_id).__name__}")
    if camera_id < 0:
        raise ValueError(f"camera_id must be >= 0, got {camera_id}")
    return camera_id


def validate_hfov_deg(hfov) -> float:
    if isinstance(hfov, bool) or not isinstance(hfov, (int, float)):
        raise ValueError(f"hfov must be a number, got {type(hfov).__name__}")
    hfov_f = float(hfov)
    if not math.isfinite(hfov_f) or hfov_f <= 0.0 or hfov_f > 180.0:
        raise ValueError(f"hfov must be finite in (0, 180], got {hfov_f!r}")
    return hfov_f
