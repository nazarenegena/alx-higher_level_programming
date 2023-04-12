#!/usr/bin/python3

"""function uses builtin open function to append the mode content"""

def append_write(filename="", text=""):

    """ encoding using utf"""

    with open(filename, mode='a', encoding='utf-8') as file:

        """the write method"""
        file.write(text)
        return len(text)
