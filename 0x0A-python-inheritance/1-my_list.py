#!/usr/bin/python3
"""
Module function/classes:
    * class MyList(list):
"""


class MyList(list):
    """
    class MyList that inherits from list
    """

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        new = sorted(self)
        print(new)
