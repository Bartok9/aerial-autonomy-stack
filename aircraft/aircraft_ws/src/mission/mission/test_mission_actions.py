#!/usr/bin/env python3
import unittest

from mission_actions import KNOWN_ACTIONS, is_known_mission_action


class TestMissionActions(unittest.TestCase):
    def test_known(self):
        for name in ("takeoff", "land", "wait", "offboard"):
            self.assertTrue(is_known_mission_action(name))

    def test_unknown(self):
        self.assertFalse(is_known_mission_action("fly_to_moon"))
        self.assertFalse(is_known_mission_action(""))
        self.assertFalse(is_known_mission_action(None))
        self.assertFalse(is_known_mission_action(1))

    def test_frozen_set_size(self):
        self.assertEqual(len(KNOWN_ACTIONS), 8)


if __name__ == "__main__":
    unittest.main()
