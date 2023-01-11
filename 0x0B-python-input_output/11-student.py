#!/usr/bin/python3
"""
Module class:
    * class Student
"""


class Student:
    """
    class Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return dict(filter(
            lambda item: item[0] in attrs, self.__dict__.items()
        ))

    def reload_from_json(self, json):
        for k, v in json.items():
            self.__setattr__(k, v)
