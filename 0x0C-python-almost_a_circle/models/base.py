#!/usr/bin/python3
class Base:

    """ private attr with value 0 """
    __nb_objects = 0

    """ the base class constructor """
    def __init__(self, id=None):
        
        """ checking for the value of id """
        if id is not None: 
           self.id = id

        else :
           
           """ incrementing the value of id per instantiation """   
           Base.__nb_objects += 1
           self.id = Base.__nb_objects   
