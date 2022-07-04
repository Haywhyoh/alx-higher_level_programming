#!/usr/bin/python3
def lookup(obj):
    """A function that returns the list of available attributes
        and methods of an object.

        Args:
            obj: The object class parameter
            
        Returns: List of the method and attributes."""
    return(dir(obj))
    