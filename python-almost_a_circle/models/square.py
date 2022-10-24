#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Special Rectangle, who has the same attributes and same methods.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiation of class

        Args:
            size: size of the square
            x: position in x
            y: position in y
            id: instance identifier
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    """ size getter and setter """
    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def __str__(self):
        """
        Returns Square description
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__width}"

    def update(self, *args, **kwargs):
        """
        Assigns attributes

        Args:
            args: arguments
        """
        if args is not None and len(args) > 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                return
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.__width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square
        """

        dict = {
            "id": self.id,
            "size": self.__width,
            "x": self.x,
            "y": self.y
        }

        return dict
