#!/usr/bin/python3
"""This is a Rectangle class"""


class Rectangle:
    """Class to create a Rectangle object"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the rectangle object"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for the width value"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif (value < 0):
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter for the height value"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif (value < 0):
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Returns the area of the Rectangle"""
        return(self.__width * self.height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Print the rectangle with #"""
        if self.__height == 0 or self.__width == 0:
            return ''
        hash_width = '#' * self.__width
        return '\n'.join((hash_width) for height in range(self.__height))

    def __repr__(self):
        """Returns a string representation of
        the rectangle instance"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        Rectangle.number_of_instances += 1
        print("Bye rectangle...")
