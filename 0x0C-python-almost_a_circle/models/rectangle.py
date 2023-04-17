#!/usr/bin/python3

from models.base import Base

""" instance of rectangle class"""

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
    def set_width(self, value):
         self._width = value
    
    """get height value"""
    @property
    def height(self):
        return self._height
    
    """ set height value"""
    @height.setter
    def set_height(self, value):
         self._height = value
      
    """get x value"""
    @property
    def x(self):
        return self._x
    
    """ set x value"""
    @x.setter
    def x(self, value):
         self._x = value
     
    """get y value"""
    @property
    def y(self):
        return self._y
    
    """ set y value"""
    @y.setter
    def y(self, value):
         self._y = value
   

