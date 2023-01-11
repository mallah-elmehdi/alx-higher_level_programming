#!/usr/bin/python3
"""
Module functions:
    * load_from_json_file(filename)
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”

    Args:
        -> my_obj: python class
        -> filename: file name

    Return: void
    """

    with open(file=filename, mode="r") as file:
        return json.loads(file.read())
