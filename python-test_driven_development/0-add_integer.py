#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        result = int(a) + (b)
    except TypeError:
        if type(a) is not int:
            raise TypeError("a must be an integer")
        if type(b) is not int:
            raise TypeError("b must be an integer") 
    return result