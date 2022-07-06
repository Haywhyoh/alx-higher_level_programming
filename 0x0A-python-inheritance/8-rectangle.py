#1/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""A module for Rectangular operations"""


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
