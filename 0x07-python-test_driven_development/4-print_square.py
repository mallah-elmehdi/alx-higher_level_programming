#!/usr/bin/python3
"""
Module function:
    * print_square(size):
"""


def print_square(size):
    """
    Given the size, print a s filled square with '#' character.

    Params:
        -> size : int

    Return: void
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print(size * "#")
