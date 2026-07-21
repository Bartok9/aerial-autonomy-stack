#!/usr/bin/env python3
"""Offline unit tests for extract_spherical_coords (no Gazebo)."""
import tempfile
import unittest
from pathlib import Path

from extract_spherical_coords import parse_spherical_coordinates


class TestParseSpherical(unittest.TestCase):
    def _write(self, body: str) -> str:
        f = tempfile.NamedTemporaryFile("w", suffix=".sdf", delete=False)
        f.write(body)
        f.close()
        return f.name

    def test_full_coords(self):
        path = self._write(
            """<?xml version="1.0"?>
            <sdf version="1.6"><world name="w">
              <spherical_coordinates>
                <latitude_deg>47.4</latitude_deg>
                <longitude_deg>8.5</longitude_deg>
                <elevation>412</elevation>
              </spherical_coordinates>
            </world></sdf>"""
        )
        lat, lon, elev = parse_spherical_coordinates(path)
        self.assertEqual(lat, "47.4")
        self.assertEqual(lon, "8.5")
        self.assertEqual(elev, "412")
        Path(path).unlink(missing_ok=True)

    def test_missing_children_default_zero(self):
        path = self._write(
            """<?xml version="1.0"?>
            <sdf version="1.6"><world name="w">
              <spherical_coordinates/>
            </world></sdf>"""
        )
        self.assertEqual(parse_spherical_coordinates(path), ("0", "0", "0"))
        Path(path).unlink(missing_ok=True)

    def test_missing_element_raises(self):
        path = self._write(
            """<?xml version="1.0"?>
            <sdf version="1.6"><world name="w"></world></sdf>"""
        )
        with self.assertRaises(ValueError):
            parse_spherical_coordinates(path)
        Path(path).unlink(missing_ok=True)

    def test_bad_file_raises(self):
        with self.assertRaises(ValueError):
            parse_spherical_coordinates("/no/such/file.sdf")


if __name__ == "__main__":
    unittest.main()
