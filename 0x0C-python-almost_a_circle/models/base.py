#!/usr/bin/python3


class Base:

    """ private attr with value 0 """
    __nb_objects = 0

    """ the base class constructor """
    def __init__(self, id=None):

        """ checking for the value of id """
        if id is not None:
           self.id = id

        else :

           """ incrementing the value of id per instantiation """
           Base.__nb_objects += 1
           self.id = Base.__nb_objects


    """ takes a list of dictionaries as inputs"""
    @staticmethod
    def to_json_string(list_dictionaries):

        """if none return []"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            """ convert the dictionary to json"""
            return json.dumps(list_dictionaries)

    """ convert json string to file"""
    @classmethod
    def save_to_file(cls, list_objs):
        """ create file name based on class name"""
        """ create a new list of objects"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"

        objects = []

        """ populate with dict representations"""
        for obj in list_objs:

            objects.append(obj.to_dictionary())

        """ write json string implememtations in the file"""
        with open(filename, "w") as file:

            file.write(Base.to_json_string(objects))

    """ convert from json string to dictionary"""
    @staticmethod
    def from_json_string(json_string):

        """ returns the list represented by the JSON string """
        """ checking if json string is empty"""

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    """ converts from dictionary to instance """
    @classmethod
    def create(cls, **dictionary):

        if cls.__name__ == "Rectangle":

            dummy = cls(1, 1)

        elif cls.__name__ == "Square":

            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)

        return dummy

    """ convert file to instances """
    filename = str(cls.__name__) + ".json"

    """ the try catch method"""
    try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                [cls.create(**d) for d in list_dicts]
    except IOError:
        []

