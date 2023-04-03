#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representing the  rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
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
        
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        rectang = ''
        for i in range(self.__height):
            rectang += '#' * self.__width
            if i != self.__height - 1:
                rectang += '\n'
        return rectang
        
    def __repr__(self):
         return eval((f"Rectangle({self.width}, {self.height})"))
         
     def __del__(self):
        print("Bye rectangle...")
