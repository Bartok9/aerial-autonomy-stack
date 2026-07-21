#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET


def parse_spherical_coordinates(sdf_file):
    """Parse spherical_coordinates from an SDF world file.

    Returns (latitude, longitude, elevation) as strings from the file
    (defaults "0" when a child element is missing).
    Raises ValueError if spherical_coordinates is absent or the file is unreadable.
    """
    try:
        tree = ET.parse(sdf_file)
    except Exception as e:
        raise ValueError(f"Error parsing SDF file: {e}") from e
    root = tree.getroot()
    spherical_coords = root.find(".//spherical_coordinates")
    if spherical_coords is None:
        raise ValueError("spherical_coordinates element not found")
    latitude = spherical_coords.findtext("latitude_deg", "0")
    longitude = spherical_coords.findtext("longitude_deg", "0")
    elevation = spherical_coords.findtext("elevation", "0")
    return latitude, longitude, elevation


def extract_spherical_coordinates(sdf_file):
    # Extract spherical coordinates from an SDF world file.
    # Returns: lat,lon,elev,0
    try:
        latitude, longitude, elevation = parse_spherical_coordinates(sdf_file)
        print(f"{latitude},{longitude},{elevation},0")
    except ValueError as e:
        if "not found" in str(e):
            print("0,0,0,0", file=sys.stderr)
            sys.exit(1)
        print(f"Error parsing SDF file: {e}", file=sys.stderr)
        print("0,0,0,0")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: extract_spherical_coords.py <sdf_file>", file=sys.stderr)
        sys.exit(1)

    extract_spherical_coordinates(sys.argv[1])
