#!/usr/bin/python3

""" This is a function that takes a filename as input """
import json

def load_from_json_file(filename):
    """
    this reads an object from the JSON file.

    filename: This is the name of the file to read from.

    Returns: this is a Python data structure represented by the JSON in the file.
    """
    with open(filename, 'r') as f:
        return json.load(f)

