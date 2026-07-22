#!/usr/bin/env python3
import os
import unittest

try:
    from drone_traffic_controller.count_env import parse_nonneg_int_env
except ImportError:
    from count_env import parse_nonneg_int_env


class TestCountEnv(unittest.TestCase):
    def setUp(self):
        self._keys = ["NUM_QUADS", "num_quads", "NUM_VTOLS", "num_vtols"]
        self._backup = {k: os.environ.get(k) for k in self._keys}
        for k in self._keys:
            os.environ.pop(k, None)

    def tearDown(self):
        for k, v in self._backup.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v

    def test_default(self):
        self.assertEqual(parse_nonneg_int_env("NUM_QUADS", "num_quads", default="1"), 1)

    def test_primary(self):
        os.environ["NUM_QUADS"] = "3"
        self.assertEqual(parse_nonneg_int_env("num_quads", "NUM_QUADS", default="1"), 3)

    def test_fallback(self):
        os.environ["num_vtols"] = "2"
        self.assertEqual(parse_nonneg_int_env("NUM_VTOLS", "num_vtols", default="0"), 2)

    def test_reject(self):
        for bad in ("", "-1", "01", "1.5", "abc", "+2"):
            os.environ["NUM_QUADS"] = bad
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    parse_nonneg_int_env("NUM_QUADS", default="0")


if __name__ == "__main__":
    unittest.main()
