#!/usr/bin/python3
"""
function that contains the class
"""

class Student:

    """this is a representation of a student class"""

    def __init__(self, first_name, last_name, age):

        """ the initialization of the student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """ this returns value of a dictionary """

        return self.__dict__
