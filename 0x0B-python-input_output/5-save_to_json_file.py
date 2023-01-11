#!/usr/bin/python3
"""
Module functions:
    * save_to_json_file(my_obj, filename)
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file,
    using a JSON representation

    Args:
        -> my_obj: python class
        -> filename: file name

    Return: void
    """

    with open(file=filename, mode="w") as file:
        file.write(json.dumps(my_obj))
