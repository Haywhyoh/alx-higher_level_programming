#!/usr/bin/python3
""" Class to define a square"""


class Square:
    """ Create class instances """

    def __init__(self, size=0):
        """Method to declare Square private instances
        Args:
                size(int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif(size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
