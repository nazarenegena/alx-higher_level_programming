#!/usr/bin/python3
"""
this contains both the BaseGeometry and subclass Rectangle
"""


class BaseGeometry:

    """this is a class that has a public instance methods area as well as an integer_validator"""

    def area(self):

        """raises an exception when instantiated"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """the condition validates if the value is an integer greater than 0"""

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    """this is a representation of the rectangle"""

    def __init__(self, width, height):

        """this is an instantiation of a rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):

        """this returns an area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):

        """this is an informal string representation of the rectangle above"""

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):

    """this is a representation of the square"""

    def __init__(self, size):

        """the instantiation of the square class"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"return the value of the area of the square instance"""
        return self.__size ** 2

    def __str__(self):
        """this is an informal string reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
