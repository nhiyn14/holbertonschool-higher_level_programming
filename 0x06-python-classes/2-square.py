#!/usr/bin/python3
"""Create a class with Exceptions"""


class Square:
    """Defines a square

    Attributes:
        __size (int): Square size
    """
    def __init__(self, size):
        """Make size Private instance attribute

        Args:
            size (int): Square size

        Return: None
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if type(size) is int and size < 0:
            raise ValueError("size must be >= 0")
