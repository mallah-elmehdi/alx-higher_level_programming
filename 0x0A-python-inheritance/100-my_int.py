#!/usr/bin/python3
"""
Module function/classes:
    * class MyInt(int)
"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __init__(self, value):
        self.value = value

    def __eq__(self, value):
        return self.value != value

    def __ne__(self, value):
        return self.value == value
