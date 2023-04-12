#!/usr/bin/python3

"""
the function contains the class_to_json function
"""

def class_to_json(obj):
    """
    Returning the dictionary description that has a simple data structure for JSON.

    Returns: the dictionary with a simple data structure.
    """
    return obj.__dict__
