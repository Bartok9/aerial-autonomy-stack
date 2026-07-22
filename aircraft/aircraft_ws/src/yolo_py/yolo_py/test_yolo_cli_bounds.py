#!/usr/bin/env python3
import math
import unittest

try:
    from yolo_py.yolo_cli_bounds import validate_camera_id, validate_hfov_deg
except ImportError:
    from yolo_cli_bounds import validate_camera_id, validate_hfov_deg


class TestYoloCliBounds(unittest.TestCase):
    def test_camera_ok(self):
        self.assertEqual(validate_camera_id(0), 0)
        self.assertEqual(validate_camera_id(3), 3)

    def test_camera_bad(self):
        for bad in (-1, True, 1.5, "0", None):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    validate_camera_id(bad)

    def test_hfov_ok(self):
        self.assertEqual(validate_hfov_deg(100), 100.0)
        self.assertEqual(validate_hfov_deg(180), 180.0)

    def test_hfov_bad(self):
        for bad in (0, -1, 180.1, math.nan, math.inf, True, "90", None):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    validate_hfov_deg(bad)


if __name__ == "__main__":
    unittest.main()
