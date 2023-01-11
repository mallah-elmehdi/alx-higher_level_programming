#!/usr/bin/python3
"""
Module function/classes:
    * is_kind_of_class(obj, a_class)
"""


def inherits_from(obj, a_class):
    """
    object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        -> obj: object
        -> a_class: class
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
