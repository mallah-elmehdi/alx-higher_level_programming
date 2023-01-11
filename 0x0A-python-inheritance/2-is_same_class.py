#!/usr/bin/python3
"""
Module function/classes:
    * is_same_class(obj, a_class):
"""


def is_same_class(obj, a_class):
    """
    object is exactly an instance of the specified class

    Args:
        -> obj: object
        -> a_class: class
    """

    return type(obj) is a_class
