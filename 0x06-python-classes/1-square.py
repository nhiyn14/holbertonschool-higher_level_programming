#!/usr/bin/python3
"""Create a class with a Private instance attribute"""


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
