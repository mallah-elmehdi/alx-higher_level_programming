#!/usr/bin/python3
"""Module documentation: Rectangle"""


class Rectangle:
    """Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Rectangle object constructor.

        Args:
            width (int): width of rect
            height (int): height of rect
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @width.setter
    def width(self, value):
        """width setter"""
        if isinstance(value, int) == False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if isinstance(value, int) == False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
