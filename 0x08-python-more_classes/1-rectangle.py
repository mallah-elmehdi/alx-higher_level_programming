#!/usr/bin/python3
"""Module documentation: Rectangle"""


class Rectangle:
    """empty class Rectangle"""

    # ----------------- constructor
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # ----------------- gettes
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    # ----------------- setters
    @width.setter
    def width(self, value):
        if isinstance(value, int) == False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if isinstance(value, int) == False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
