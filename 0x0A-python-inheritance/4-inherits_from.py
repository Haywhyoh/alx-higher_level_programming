#!/usr/bin/python3
"""The modeule check for the instance of an object"""


def inherits_from(obj, a_class):
    """This function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
     the specified class.

     Args:
        obj: The object class.
        a_class: the class to be tested.

    Returns: True id the object is an instance or if the object
    is an instance of a class that inherited from."""
    return issubclass(obj, a_class)
