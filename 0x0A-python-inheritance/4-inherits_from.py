#!/usr/bin/python3

"""function to check isinstance of a value"""

def inherits_from(obj, a_class):
    """
    Return the value True if the obj is an instance of a class that inherited
    either directly or indirectly from a_class if not return value False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

