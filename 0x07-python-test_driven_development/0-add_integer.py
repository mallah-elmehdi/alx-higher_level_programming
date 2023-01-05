#!/usr/bin/python3
"""
Module function:
    * add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    Given two integers, return the sum i.e (a + b).

    Params:
        -> a : int or float
        -> b : int or float

    Return: int
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
add_integer(1, int(float('')))