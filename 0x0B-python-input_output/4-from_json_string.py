#!/usr/bin/python3
"""Input and output python module."""
import json


def from_json_string(my_str):
    """ Function that returns an object (Python data structure)
        represented by a JSON string.

        Args:
            my_str: the string to be converted

        Returns:
            an object (Python data structure."""
    return json.loads(my_str)
