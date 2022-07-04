#!/usr/bin/python3
"""The module or an obj class"""


def is_same_class(obj, a_class):
    """Function checks if the object is exactly
    an instance of the specified class.

    Args:
        a_class: the instance to be checked
        object: the object class

    Returns: True if the is object is an instance,
            and false otherwise
    """
    return type(obj) is a_class
