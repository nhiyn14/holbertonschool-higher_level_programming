#!/usr/bin/python3
"""
Class Base
"""


import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init an instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation of list_objs to a file"""
        fileName = cls.__name__ + ".json"
        newFile = []
        if list_objs is not None:
            for i in list_objs:
                newFile.append(cls.to_dictionary(i))
        with open(fileName, 'w', encoding="utf-8") as w:
            w.write(cls.to_json_string(newFile))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return {}
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        if cls.__name__ == "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance
