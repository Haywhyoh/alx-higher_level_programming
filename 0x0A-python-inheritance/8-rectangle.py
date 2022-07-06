#1/usr/bin/python3
"""A module for Rectangular operations"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class to create and manipulate rectangle object"""

    def __init__(self, width, height):
        """initializer
        Args
           width
           height
        """
        self.integer_validator('width', width)
        self.__width__ = width
        self.integer_validator('height', height)
        self.__height__ = height

