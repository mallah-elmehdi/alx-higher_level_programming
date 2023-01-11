#!/usr/bin/python3
"""
Module function:
    * lookup(obj)
"""


def lookup(obj):
    """
    function that returns the list of
    available attributes and methods of an object.

    Params:
        -> obj : object

    Return: list
    """

    return (dir(obj))
