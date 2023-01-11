#!/usr/bin/python3
"""
Module function/classes:
    * is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """
    object is an instance of, or if the object is
    an instance of a class that inherited from

    Args:
        -> obj: object
        -> a_class: class
    """

    return isinstance(obj, a_class)
