#!/usr/bin/python3
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
        self.integer_validator("width", width)
        self.__width__ = width
        self.integer_validator('height', height)
        self.__height__ = height

    def area(self):
        """area of rectangle"""
        return(self.__height * self.__width)

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
