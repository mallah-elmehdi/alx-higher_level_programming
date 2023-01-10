#!/usr/bin/python3
"""
Module function:
    * add_integer(a, b)
"""


def lookup(obj):
    """
    function that returns the list of available attributes and methods of an object.

    Params:
        -> obj : object

    Return: list
    """

    return (dir(obj))
