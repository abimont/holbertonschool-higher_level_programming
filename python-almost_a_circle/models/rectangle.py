#!/usr/bin/python3
"""
Class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

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

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    """ height getter and setter """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    """ x getter and setter """
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    """ y getter and setter """
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def __str__(self):
        """
        Returns Rectangle's description
        """
        return f"[Rectangle] ({self.id}) {self.__x}/\
{self.__y} - {self.__width}/{self.__height}"

    def area(self):
        """
        Returns the area value of the Rectangle instance
        """
        return self.__height * self.__width

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #
        at position given by x and y
        """
        [print() for y in range(self.__y)]
        for line in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            for element in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        Public method that assigns an argument to each attribute

        Args:
            args: arguments passed to the function
        """
        if args is not None and len(args) > 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                return
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        dict_rep = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }

        return dict_rep
