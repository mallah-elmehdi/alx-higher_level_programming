#!/usr/bin/python3
"""
Module functions:
    * to_json_string(my_obj)
"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)

    Args:
        -> my_obj: python obj

    Return: JSON string
    """

    return json.dumps(my_obj)
