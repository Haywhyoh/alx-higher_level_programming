#!/usr/bin/python3
"""A square module. """


class Square:
    """ A class to define square properties."""

    def __init(self, size):
        """
            Method to initialize size

            Args:
                size(int): The size of the squre
        """
        self.__size = size

    @property
    def size(self):
        """
            method to get the value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            Method to set variable
        """
        if value < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    def area(self):
        """
        Method to calculate area
        """
        return (self.__size ** 2)

    def my_print(self, size=0):
        """
            Method to print # in square
            according to the size value
        """
        if self.__size = 0:
            print()
        for width in range(self.__size):
            for length in range(self.__size):
                print('#', end='')
            print()
