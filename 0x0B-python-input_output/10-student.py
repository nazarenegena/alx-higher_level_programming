#!/usr/bin/python3
"""function defines the student class."""


class Student:

    """this represents a student class."""

    def __init__(self, first_name, last_name, age):

        """ to initialize a new Student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """getting a dictionary representation of the Student class."""

        if (type(attrs) == list and

                all(type(ele) == str for ele in attrs)):

            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__
