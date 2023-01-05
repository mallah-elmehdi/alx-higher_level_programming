#!/usr/bin/python3
"""
Module function:
    * say_my_name(first_name, last_name=""):
"""


def say_my_name(first_name, last_name=""):
    """
    Given two string, print a message.

    Params:
        -> first_name : string
        -> last_name : string

    Return: void
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
