#!/usr/bin/python3
"""
Module functions:
    * append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """
    appends a string to a text file (UTF8) and
    returns the number of characters added

    Args:
        -> filename: str
        -> text: str

    Return: int
    """

    with open(file=filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
