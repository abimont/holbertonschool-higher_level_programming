#!/usr/bin/python3
""" Writes a string to a text file """


def write_file(filename="", text=""):
    """
    Writes a string from filename to text (UTF8)
    and returns the number of characters written

    Args:
        filename: file to read the string
        text: file to write thw string
    """

    with open(filename, 'w', encoding='UTF8') as file:
        chars_writt = file.write(text)

    return chars_writt
