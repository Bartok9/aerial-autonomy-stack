#!/usr/bin/env python3
import unittest

from inspect_topics_parse import parse_topic_info_lines


SAMPLE = """
Type: sensor_msgs/msg/Image
Publisher count: 1
Node name: cam_node
Node namespace: /
Subscription count: 2
Node name: viewer
Node namespace: /
Node name: _ros2cli_123
Node namespace: /
Node name: UNKNOWN
Node namespace: /
""".strip().splitlines()


class TestInspectTopicsParse(unittest.TestCase):
    def test_sample(self):
        parsed = parse_topic_info_lines(SAMPLE)
        self.assertEqual(parsed["msg_type"], "sensor_msgs/msg/Image")
        self.assertEqual(parsed["pubs"], ["cam_node"])
        self.assertEqual(parsed["subs"], ["viewer"])

    def test_empty(self):
        parsed = parse_topic_info_lines([])
        self.assertEqual(parsed["msg_type"], "Unknown")
        self.assertEqual(parsed["pubs"], [])
        self.assertEqual(parsed["subs"], [])

    def test_type_only(self):
        parsed = parse_topic_info_lines(["Type: std_msgs/msg/String"])
        self.assertEqual(parsed["msg_type"], "std_msgs/msg/String")


if __name__ == "__main__":
    unittest.main()
