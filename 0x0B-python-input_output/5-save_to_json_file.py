#!/usr/bin/python3

"""this is a function takes an object and a filename as input"""

import json

"""function writes the JSON representation of the object to the file."""

def save_to_json_file(my_obj, filename):
    """
    Writing an object to a text file using its JSON representation.

    Args:
        my_obj: The object that is to write to the file.
        filename: and the filename is name of the file to write to.

    Returns:None or Null.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

