#!/usr/bin/python3
"""Input and output python module."""
import json


def load_from_json_file(filename):
    """ Function that creates an Object from a “JSON file”

        Args:
            my_obj: the object to be written into a file
            filename: the file the JSON is written into.

        Returns:
            an object."""
    with open(filename, encoding='utf-8') as my_file:
       return (json.load(my_file))
