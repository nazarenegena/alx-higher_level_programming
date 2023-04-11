#!/usr/bin/python3
""" this defines a function that adds the attributes to the objects"""

def add_new_attribute(obj, name, value):

    """adds the new attribute to an object and raises a
        typeError
    """

    if hasattr(obj, '__dict__'):
        obj.__dict__[name] = value

    else:
        raise TypeError("can't add new attribute")
