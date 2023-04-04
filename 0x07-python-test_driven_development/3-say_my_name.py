#!/usr/bin/python3
""" function that prints first and last name"""
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print ("Hello there, I am {} {}" .format(first_name, last_name))
