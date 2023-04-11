#!/usr/bin/python3
"""
Has the class BaseGeometry as well as the subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """this is a representation of a square"""

    def __init__(self, size):

        """an instantiation of a square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):

        """the return value is the area of the square"""

        return self.__size ** 2
