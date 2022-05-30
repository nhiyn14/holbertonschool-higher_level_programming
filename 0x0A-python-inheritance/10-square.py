#!/usr/bin/python3
"""
a subclass inhrits from a subclass of a specific class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass of Rectangle"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of Square"""
        return self.__size * self.__size
