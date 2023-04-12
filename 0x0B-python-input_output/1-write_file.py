#!/usr/bin/python3
""" the function has two parameters"""

def write_file(filename="", text=""):

    """ the with statement to ensure the file is properly closed """

    """ the encoding param to ensure file is writen as utf"""

    with open(filename, 'w', encoding='utf-8') as f:

        written_file = f.write(text)

    return written_file
