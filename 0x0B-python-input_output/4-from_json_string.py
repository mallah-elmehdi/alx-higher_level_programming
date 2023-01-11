#!/usr/bin/python3
"""
Module functions:
    * from_json_string(my_str)
"""
import json


def from_json_string(my_str):
    """
    returns an object (Python data structure)
    represented by a JSON string

    Args:
        -> my_str: JSON string

    Return: python obj
    """

    return json.loads(my_str)
