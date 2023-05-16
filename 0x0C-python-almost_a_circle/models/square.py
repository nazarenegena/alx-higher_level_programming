#!/usr/bin/python3
""" inheriting from Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ the Square class """

    def __init__(self, size, x=0, y=0, id=None):

        """ constructor of the square class"""

        super().__init__(size, size, x, y, id)

        self.size = size

    @property
    def size(self):

        """ Defining  the size attribute """
        """ getter method """

        return self.width

    @size.setter
    def size(self, value):

        """ Defining the size behavior """
        """ the setter value"""

        self.width = value

        self.height = value

    def __str__(self):
        """ Setting standard values for print """

        si_id = "({}) ".format(self.id)

        si_xy = "{}/{} - ".format(self.x, self.y)

        si_size = "{}".format(self.size)

        return "[Square] " + si_id + si_xy + si_size

    def update(self, *args, **kwargs):

        """ Updating the functions attributes """

        if args is not None and len(args) > 0:

            att = ["id", "size", "x", "y"]

            for j in range(len(args)):
                setattr(self, att[j], args[j])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ this returns a dictionary representation """
        k = {
            'id': self.id, 'size': self.size,
            'x': self.x, 'y': self.y
        }

        return k
