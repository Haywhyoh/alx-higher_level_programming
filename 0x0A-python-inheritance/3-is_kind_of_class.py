#!/usr/bin/python3
"""The modeule check for the instance of an object"""


def is_kind_of_class(obj, a_class):
    """This function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
     the specified class.

     Args:
        obj: The object class.
        a_class: the class to be tested.

    Returns: True id the object is an instance or if the object
    is an instance of a class that inherited from."""
    return isinstance(obj, a_class)
