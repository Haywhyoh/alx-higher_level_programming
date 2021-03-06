#!/usr/bin/python3
"""Input and output python module."""
import json


def to_json_string(my_obj):
    """Function that returns the JSON representation
        of an object (string):

        Args:
            my_obj: the object to be converted

        Returns:
            JSON representation of the my_obj."""
    return (json.dumps(my_obj))
