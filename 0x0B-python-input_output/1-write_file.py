#!/usr/bin/python3
"""
Module functions:
    * write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        -> filename: str
        -> text: str

    Return: int
    """

    with open(file=filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
