#!/usr/bin/python3
"""
Module function:
    * def text_indentation(text)
    * def get_new_str(text, delim):
"""


def get_new_str(text, delim):
    return f'{delim}\n\n'.join(
        map(lambda line: line.strip(), text.split(delim))
    )


def text_indentation(text):
    """
    Given two string, prints a text with 2 new lines after each
    of these characters: '.', '?' and ':'

    Params:
        -> text : string

    Return: void
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ['?', ".", ":"]:
        text = get_new_str(text, delim)

    print(text, end="")
