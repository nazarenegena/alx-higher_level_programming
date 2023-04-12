#!/usr/bin/python3

def class_to_json(obj):
    """
    Returning the dictionary description that has a simple data structure for JSON.

    Returns: the dictionary with a simple data structure.
    """

    """ Getting the dictionary representation of object's attributes """
    attrDict = obj.__dict__

    """ Creating a new dictionary with the serializable values """

    serializableDict = {}

    for key, value in attrDict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializableDict[key] = value

    return serializableDict

