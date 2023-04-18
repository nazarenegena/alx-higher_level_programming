#!/usr/bin/python3

from models.rectangle import Rectangle

""" inheriting from Rectangle class"""

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    """assigning attributes to key value pairs"""
    
    def update(self, *args, **kwargs):
        
        """ args initiates the attributes"""
        """ the kwargs : is the attribute of key value pairs"""

        if args and len(args) != 0:
            j = 0
            for arg in args:
                if j == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif j == 1:
                    self.size = arg
                elif j == 2:
                    self.x = arg
                elif j == 3:
                    self.y = arg
                j += 1

        elif kwargs and len(kwargs) != 0:
            for h, q in kwargs.items():
                if h == "id":
                    if q is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = q
                elif h == "size":
                    self.size = q
                elif h == "x":
                    self.x = q
                elif h == "y":
                    self.y = q

    
   
