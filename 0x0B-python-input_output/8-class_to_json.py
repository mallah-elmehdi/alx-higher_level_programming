#!/usr/bin/python3
"""
Module functions:
    * def class_to_json(obj):
"""


def class_to_json(obj):
    """
    creates an Object from a “JSON file”

    Args:
        -> my_obj: python class
        -> filename: file name

    Return: void
    """

    return obj.__dict__
