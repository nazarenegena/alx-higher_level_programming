#!/usr/bin/python3

import sys

from save_to_json_file import save_to_json_file

from load_from_json_file import load_from_json_file


""" Defining the name of the file to save the list to """

filename = 'add_item.json'

""" Loading the existing list from the file """
try:
    my_list = load_from_json_file(filename)

except:

    my_list = []

""" Adding the command-line arguments to the list """

my_list.extend(sys.argv[1:])

""" Save the updated list to the file """

save_to_json_file(my_list, filename)
