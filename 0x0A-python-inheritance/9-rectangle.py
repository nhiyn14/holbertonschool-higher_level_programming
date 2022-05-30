#!/usr/bin/python3
"""
a subclass of a specific class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass of BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Inherit area() from BaseGeometry"""
        return self.__width * self.__height

    def __str__(self):
        return(f"[Rectangle] {self.__width}/{self.__height}")
