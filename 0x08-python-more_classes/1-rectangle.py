#!/usr/bin/python3
"""Create class Rectangle with Private attribute: width and height"""


class Rectangle:
    """Define Rectangle

    Attributes:
        width: Width of Rectangle
        height: Height of Rectangle
    """
    def __init__(self, width=0, height=0):
        """Init instance with class Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter property to retrive __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter property for __width to value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter property to retrive __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter property for __height to value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
