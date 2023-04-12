#!/usr/bin/python3
"""
function contains the append after function
"""


def append_after(filename="", search_string="", new_string=""):

    """ this appends the new string after a line with string filename """

    with open(filename, 'r', encoding='utf-8') as f:

        linedList = []

        while True:

            line = f.readline()

            if line == "":
                break
            linedList.append(line)

            if search_string in line:

                linedList.append(new_string)

    with open(filename, 'w', encoding='utf-8') as f:

        f.writelines(linedList)

