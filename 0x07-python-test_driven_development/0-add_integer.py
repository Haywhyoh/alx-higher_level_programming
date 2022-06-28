#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Function to add two integers or float numbers

        Args:
            a: first number
            b: second number
        
        Return: 
            The sum of both number as an integers

        Raises:
            TypeError if a or b is not int or float

    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
