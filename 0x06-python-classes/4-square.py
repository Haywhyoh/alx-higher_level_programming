#!/usr/bin/python3
"""
    Class to create a ssquare
"""


class Square:
    """
        Class for the square object

        Args:
            size: size of a square
    """

    def __init__(self, size=0):
        """
            Initialize the size
        """
        self.__size = size

    @property
    def __init__(self, size=0):
        """
            get the size
        """
        return (self.__size)

    @size.setter
    def __init__(self, size=0):
        """
            set the size
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError('size must be >= 0')
        self__size = size

    def area(self):
        """
        Calculates the area of a square
        """
        return (self.__size ** 2)
