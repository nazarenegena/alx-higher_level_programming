#!/usr/bin/python3
def lookup(obj):
    # Getting  a list of all attributes & methods of the object
    attributes_and_methods_lists = dir(obj)

    # Returning the filtered list
    return attributes_and_methods_lists
