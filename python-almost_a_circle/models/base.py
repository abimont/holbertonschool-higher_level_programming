#!/usr/bin/python3
"""
Class Base
"""


import json


class Base:
    """
    Base class for all other classes in this project
    Goal: to manage id attribute in all future classes and
    to avoid duplicating the same code
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor

        Args:
            id: id of the class. If id is None, increment __nb_objects and
            assign the new value to the public instance attribute id
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries: list of dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        Args:
            list_objs: list of instances who inherits of Base
        """

        filename = cls.__name__ + ".json"
        list = []
        if list_objs is not None:
            for obj in list_objs:
                list.append(cls.to_dictionary(obj))
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string

        Args:
            json_string: string representing a list of dictionaries
        """

        if json_string is None or len(json_string) <= 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set

        Args:
            dictionary: keyworded arguments
        """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list = Base.from_json_string(file.read())
                return [cls.create(**elem) for elem in list]
        except IOError:
            return []
