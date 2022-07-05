#!/usr/bin/python3
"""Input and output python module."""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout.

        Args:
            filename: the name of the file to be read.

        Returns:
            print file content."""
    with open(filename, encoding= 'utf-8') as my_file:
        content = my_file.read()
        print(content)
