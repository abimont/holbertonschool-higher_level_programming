#!/usr/bin/python3
"""
Class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instance of Rectangle class that inherits from Base class

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: position in x
            y: position in y
            id: instance identifier
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """ width getter and setter """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    """ height getter and setter """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    """ x getter and setter """
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    """ y getter and setter """
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
