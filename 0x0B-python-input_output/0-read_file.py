#!/usr/bin/python3
"""
Module functions:
    * read_file(filename="")
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout

    Args:
        -> filename: the file name 
    """

    with open(file=filename, mode="r", encoding="utf-8") as file:
        print(file.read())


read_file("my_file_0.txt")
