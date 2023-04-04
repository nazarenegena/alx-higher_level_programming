#!/usr/bin/python3
"""
Defining my class Rectangle
"""


class Rectangle:
    """Representing my rectangle."""
    def __init__(self, width=0, height=0, number_of_instances=0):
        """Initializing a new Rectangle.
        Args:
            width (int): new rectangle width.
            height (int): new rectangle height
        """
        self.width = width
        self.height = height
        self.number_of_instances += number_of_instances 
        
    @property
    def width(self):
        """Getter of the rectangle width."""
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
        """Returning the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectang = []
        for i in range(self.__height):
            [rectang.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rectang))

    def __repr__(self):
        """Returning the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")

