#!/usr/bin/python3
""" A square class"""


class Square:
    """Create a square object"""


    def __init__(self, size=0):
        """
        Declare private square instances

        size(int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
            Calculates the area of the square

            Returns the area of the square
        """
        return self.__size ** 2
