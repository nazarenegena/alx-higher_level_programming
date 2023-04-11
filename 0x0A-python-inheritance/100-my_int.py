#!/usr/bin/python3
"""a class that inherits from int"""

class MyInt(int):

    """ methods responsible for operators"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
