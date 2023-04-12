#!/usr/bin/python3

"""function that uses uses the built-in json module """

import json

""" this is a function takes a JSON string as input"""

def from_json_string(my_str):
    """
    Converts the JSON string to a Python data structure.

    Args:
        my_str: The JSON string to be converted.

    Returns:
        this is a Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
