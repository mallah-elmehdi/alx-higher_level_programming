#!/usr/bin/python3
"""
Module functions:
    * read_file(filename="")
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout

    Args:
        -> filename: str

    Return: void
    """

    with open(file=filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
