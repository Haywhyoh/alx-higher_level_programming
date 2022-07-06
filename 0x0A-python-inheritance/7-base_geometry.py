#!/usr/bin/python3
"""The module for the BaseGeometry Class"""


class BaseGeometry:

    """
    a class for BaseGeometry.
    """

    def area(self):
        """Function to raise an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
