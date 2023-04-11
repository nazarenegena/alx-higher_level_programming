#!/usr/bin/python3
"""contains the MyList class"""
class MyList(list):

    """list subclass"""
    def print_sorted(self):

        """initializing the object"""
        sorted_list = sorted(self)

        """printing the list"""
        print(sorted_list)
