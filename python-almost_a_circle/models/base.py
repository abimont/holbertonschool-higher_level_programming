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
