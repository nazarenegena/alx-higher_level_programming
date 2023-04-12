#!/usr/bin/python3

"""a function that uses the built-in json module to convert an object to its JSON representation as a string"""

import json

""" in this function it takes an object as an input and returns any string representing the JSON """
def to_json_string(my_obj):
    """
    Converting an object to its JSON representation as a string.

    Args:
        my_obj: The object being converted.

    Returns:
        A string value that represents the JSON representation of the object.
    """
    return json.dumps(my_obj)
