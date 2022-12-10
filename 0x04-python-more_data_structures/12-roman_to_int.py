#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    result = 0
    for i in range(len(roman_string)):
        if i + 2 < len(roman_string):
            item1 = roman_string[i]
            item2 = roman_string[i + 2]
            if roman[item2] > roman[item1]:
                result -= roman[item1]
                continue
        elif i + 1 < len(roman_string):
            item1 = roman_string[i]
            item2 = roman_string[i + 1]
            if roman[item2] > roman[item1]:
                result -= roman[item1]
                continue
        item = roman_string[i]
        result += roman[item]

    return result
