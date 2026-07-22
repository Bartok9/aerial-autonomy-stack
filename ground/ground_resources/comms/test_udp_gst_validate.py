#!/usr/bin/env python3
import unittest

from udp_gst_validate import validate_udp_port, validate_window_name


class TestUdpGstValidate(unittest.TestCase):
    def test_port_ok(self):
        self.assertEqual(validate_udp_port(5600), 5600)
        self.assertEqual(validate_udp_port(1), 1)
        self.assertEqual(validate_udp_port(65535), 65535)

    def test_port_bad(self):
        for bad in (0, -1, 65536, 1.5, True, "5600", None):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    validate_udp_port(bad)

    def test_name_ok(self):
        self.assertEqual(validate_window_name("cam0"), "cam0")
        self.assertEqual(validate_window_name("  left  "), "left")

    def test_name_bad(self):
        for bad in ("", "   ", None, 1):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    validate_window_name(bad)


if __name__ == "__main__":
    unittest.main()
