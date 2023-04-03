#!/usr/bin/python3
"""
Defining my class Rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):

         """Initializing a new Rectangle instance
        Args:
            width (int): is the width of the rectangle.
            height (int): is the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Accessor of the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Accessor of the rectangle's length"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        perim = (self.__height + self.__width)*2
        if(self.__width == 0 or self.__height == 0):
            perim = 0
        return perim
