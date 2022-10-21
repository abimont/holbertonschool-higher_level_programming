#!/usr/bin/python3
"""
Class Base
"""


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
