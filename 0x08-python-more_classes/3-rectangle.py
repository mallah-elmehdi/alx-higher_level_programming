#!/usr/bin/python3
"""Module documentation: Rectangle"""


class Rectangle:
    """Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Rectangle object constructor.

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width != 0 and self.height != 0:
            return (self.width + self.height) * 2
        return 0

    def __str__(self):
        """represents the class objects as a string"""
        ret = ""
        if self.area() != 0:
            for i in range(self.height):
                ret += "#" * self.width
                ret += "\n"
        return ret
