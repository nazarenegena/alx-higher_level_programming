#!/usr/bin/python3
def lookup(obj):
    # Getting  a list of all attributes & methods of the object
    attributes_and_methods_lists = dir(obj)

    # Filtering out any private attributes or methods
    attributes_and_methods_lists = [attr for attr in attributes_and_methods_lists if not attr.startswith('_')]

    # Returning the filtered list
    return attributes_and_methods_lists
