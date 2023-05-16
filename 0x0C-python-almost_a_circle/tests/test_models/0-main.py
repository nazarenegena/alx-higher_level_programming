#!/usr/bin/python3

""" the main file  """

from models.base import Base

""" the function to report result """

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(24)
    print(b4.id)

    b5 = Base()
    print(b5.id)
