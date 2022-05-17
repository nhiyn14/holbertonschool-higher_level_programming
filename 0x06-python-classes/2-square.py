#!/usr/bin/python3
"""Create a class with Exceptions"""


class Square:
    """Defines a square

    Attributes:
        __size (int): Square size
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """Make size Private instance attribute

        Args:
            size (int): Square size

        Return: None
        """
        self.__size = size
