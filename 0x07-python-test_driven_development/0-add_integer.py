#!/usr/bin/python3
def add_integer(a, b=98):
    """ function that adds two intergers"""
    if isinstance(a, (int,float)):
        if isinstance(b, (int, float)):
            return b
        else:
            raise TypeError('b must be an integer')
        return a
    else:
        raise TypeError('a must be an integer')
        
    """ check if they are floats"""
    if isinstance(a, float):
        a=int(a)
        if isinstance(b, float):
            b=int(b)
            return b
        return a + b
