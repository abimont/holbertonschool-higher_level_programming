#!/usr/bin/python3


def roman_to_int(roman_string):

    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    string = []
    total = 0
    prev_key = ""
    prev_val = 0

    if roman_string is None or type(roman_string) is not str:
        return 0

    for character in roman_string:
        string.append(character)

    for num in string:
        for key, value in numbers.items():
            if num == key:
                valor = value
                if prev_key == 'X' and (key == 'L' or key == 'C'):
                    valor = value - (prev_val * 2)

                if prev_key == 'I' and (key == 'V' or key == 'X'):
                    valor = value - (prev_val * 2)

                if prev_key == 'C' and (key == 'D' or key == 'M'):
                    valor = value - (prev_val * 2)

                if num == 'X' or num == 'C' or num == 'I':
                    prev_val = value
                    prev_key = key

                total += valor
                valor = 0
    return total
