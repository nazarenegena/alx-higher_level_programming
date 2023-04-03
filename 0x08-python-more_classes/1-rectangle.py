#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

     # width getter
    @property
    def width(self):
        return self.__width

    # width setter
    @width.setter
    def width(self, value):
        if type(value)is not int:
            raise TypeError("width must be an integer")
        if(value)< 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        # height getter
    @property    
    def height(self):
        return self.__height

        #height setter
    @height.setter    
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
