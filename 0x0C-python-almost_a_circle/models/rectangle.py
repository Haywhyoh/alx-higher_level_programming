#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):

    def __init__(self,  width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
         
        if width <= 0:
            raise ValueError('width must be > 0')

        self.__width = width

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')

        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return(self.__x)

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x
    
    @property
    def y(self):
        return(self.__y)

    @y.setter
    def y(self, y):
        if y < 0:
            raise ValueError('y must be >= 0')

        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        self.__y = y

    def area(self):
        return (self.__width * self.__height)
    
    def display(self):
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
    
    def __str__(self):
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))


    def update(self, *args):
        arg_list = [arg for arg in args]
        print (arg_list)
        if arg_list[0]:
            self.__width = arg_list[0]
        if arg_list[0]:
            self.__height = arg_list[1]
        self.__x = arg_list[2]
        self.__y = arg_list[3]
