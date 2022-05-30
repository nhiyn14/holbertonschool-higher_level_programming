#!/usr/bin/python3
"""
class fr 6-base_geometry + another public instance
"""


class BaseGeometry:
    """class with Public instance methods"""
    def area(self):
        """raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
