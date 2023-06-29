#!/usr/bin/python3
"""peak-finding algorithim"""

def find_peak(list_of_integers):
    """ Function that finds peak in list of ints """
    if list_of_integers == []:
        return None

    listLength = len(list_of_integers)
    mid = int(listLength / 2)
    li = list_of_integers

    if mid - 1 < 0 and mid + 1 >= listLength:
        return li[mid]
    elif mid - 1 < 0:
        return li[mid] if li[mid] > li[mid + 1] else li[mid + 1]
    elif mid + 1 >= listLength:
        return li[mid] if li[mid] > li[mid - 1] else li[mid - 1]

    if li[mid - 1] < li[mid] > li[mid + 1]:
        return li[mid]

    if li[mid + 1] > li[mid - 1]:
        return find_peak(li[mid:])
    return find_peak(li[:mid])
