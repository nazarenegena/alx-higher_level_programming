#!/usr/bin/python3
for i in range((10)+1):
    for j in range(10):
        if(i<j):
            print(f"{i}{j}".format(i,j), end=", ")
