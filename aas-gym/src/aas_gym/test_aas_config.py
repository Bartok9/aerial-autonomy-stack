#!/usr/bin/env python3
import math
import unittest

try:
    from aas_gym.aas_config import (
        validate_aas_config,
        validate_zmq_transport,
        finite_episode_seconds,
    )
except ImportError:
    from aas_config import (
        validate_aas_config,
        validate_zmq_transport,
        finite_episode_seconds,
    )


class TestAasConfig(unittest.TestCase):
    def test_defaults_ok(self):
        cfg = validate_aas_config()
        self.assertEqual(cfg["autopilot"], "px4")
        self.assertEqual(cfg["num_quads"], 1)

    def test_bad_num_quads(self):
        with self.assertRaises(ValueError):
            validate_aas_config(num_quads=0)
        with self.assertRaises(ValueError):
            validate_aas_config(num_quads=-1)

    def test_bad_odom(self):
        with self.assertRaises(ValueError):
            validate_aas_config(odom="vins-fusion")

    def test_bad_freq(self):
        with self.assertRaises(ValueError):
            validate_aas_config(gym_freq_hz=0)

    def test_zmq(self):
        self.assertEqual(validate_zmq_transport("tcp"), "tcp")
        with self.assertRaises(ValueError):
            validate_zmq_transport("udp")

    def test_episode_seconds(self):
        self.assertEqual(finite_episode_seconds(300), 300.0)
        for bad in (0, -1, math.nan, math.inf):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    finite_episode_seconds(bad)


if __name__ == "__main__":
    unittest.main()
