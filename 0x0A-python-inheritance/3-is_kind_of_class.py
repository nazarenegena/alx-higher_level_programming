#!/usr/bin/python3

"""Defines if-class-checking function"""

def is_kind_of_class(obj, a_class):
    """
    Return value is True if the object is either an instance of, or is the instance of a class that inherited from,
    the exact specified class or else return value False.
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
