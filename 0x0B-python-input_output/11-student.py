#!/usr/bin/python3
"""
function contains the class
"""


class Student:

    """ this is a representation of a student class"""

    def __init__(self, first_name, last_name, age):

        """this initializes the student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """ this returns the dictionary representation of the Student instance """

        if attrs is None:
            return self.__dict__
        newDict = {}
        for a in attrs:
            try:
                newDict[a] = self.__dict__[a]
            except FileNotFoundError:
                pass
        return newDict

    def reload_from_json(self, json):

        """this replaces all the attributes of the Student instance"""

        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
