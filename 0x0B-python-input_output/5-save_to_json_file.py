#!/usr/bin/python3
"""Input and output python module."""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file,
        using a JSON representation.

        Args:
            my_obj: the object to be written into a file
            filename: the file the JSON is written into.

        Returns:
            an object (Python data structure."""
    with open(filename, mode='w', encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
