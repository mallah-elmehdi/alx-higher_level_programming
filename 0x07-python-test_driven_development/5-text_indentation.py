#!/usr/bin/python3
"""
Module function:
    * def text_indentation(text)
"""


def text_indentation(text):
    """
    Given two string, prints a text with 2 new lines after each of these characters: '.', '?' and ':'

    Params:
        -> text : string

    Return: void
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ['?', ".", ":"]:
        text = text.replace(delim, f"{delim}\n\n")

    text = '\n\n'.join(map(lambda line: line.strip(), text.split("\n\n")))
    print(text)
