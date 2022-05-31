#!/usr/bin/python3
"""
a class Student that defines a student
"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """Create instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) is not list or attrs is None:
            return self.__dict__
        newDict = {}
        for key in attrs:
            try:
                if self.__dict__[key]:
                    newDict[key] = self.__dict__[key]
            except Exception:
                pass
        return newDict
