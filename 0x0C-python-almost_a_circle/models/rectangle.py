#!/usr/bin/python3

from models.base import Base


""" inherited from the base class"""



class Rectangle(Base):

    """ constructor with new values other than id"""

    def __init__(self, width, height, x=0, y=0, id=None):

        """ private attributes for rectangle class"""
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    """ public getter and setter functions for values"""
    """get width value"""
    @property
    def width(self):
        return self._width
    
    """ set width value"""
    @width.setter
    def width(self, value):
         if not isinstance(value, int):
             raise TypeError("width must be an integer")
         if value <= 0:
             raise ValueError("width must be > 0")
         self._width = value
    
    """get height value"""
    @property
    def height(self):
        return self._height
    
    """ set height value"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
           raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self._height = value
      
    """get x value"""
    @property
    def x(self):
        return self._x
    
    """ set x value"""
    @x.setter
    def x(self, value):
         if not isinstance(value, int):
             raise TypeError("x must be an integer")
         if value < 0:
             raise ValueError("x must be >= 0")
         self._x = value
     
    """get y value"""
    @property
    def y(self):
        return self._y
    
    """ set y value"""
    @y.setter
    def y(self, value):
         if not isinstance(value, int):
             raise TypeError("y must be an integer")
         if value < 0:
             raise ValueError("y must be >= 0")
         self._y = value

    """ public class area"""
    def area(self):
        """ calculating area of rectangle"""
        return self._height * self._width     
    
    """ public method that displays the rectangle with # character"""
    def display(self):
        for i in range(self._height):
            print("#" * self._width)
    

    """ method to update and overide the __str__ method """

    def update(self, *args, **kwargs):

        """ args initiates the attributes"""
        """ the kwargs (dict):is the attribute of key-value pairs """

        if args:
             for i, arg in enumerate(args):
                  if i == 0:  
                     if arg is None:
                          raise ValueError(" the id attribute can't be None")    
                     else:
                       self.id = arg   
                  elif i == 1:
                     self.width = arg
                  elif i == 2:
                     self.height = arg
                  elif i == 3:
                     self.x = arg
                  elif i == 4:
                     self.y = arg    
        
        elif kwargs:

            """ checking through the key value pairs """

            for k, j in kwargs.items():
              if k == "id":
                   if j is None:
                    raise ValueError("id attribute cannot be None")
                   else:
                    self.id = j

              elif k == "width":
                self.width = j
              elif k == "height":
                self.height = j
              elif k == "x":
                self.x = j
              elif k == "y":
                self.y = j

   
    def to_dictionary(self):

        """Returning the value dictionary that reps a Rectangle."""

        return {
          
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):

        """ the value to be returned is the print() and str() representation of the Rectangle."""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)      
        


