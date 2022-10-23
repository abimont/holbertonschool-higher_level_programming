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
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns Square description
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
