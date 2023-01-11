#!/usr/bin/python3
"""
Module function/classes:
    * add_attribute(obj, name, value):
"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object if it’s possible

    Args:
        -> obj: object
        -> name: attribute name
        -> value: attribute value
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
