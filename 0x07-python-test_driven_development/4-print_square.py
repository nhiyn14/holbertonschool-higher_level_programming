#!/usr/bin/python3
"""
Module to print square of #

Arguments: size
"""


def print_square(size):
    """a square with the character #
    Returns: square of #
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size > 0:
        for i in range(size):
            print("#" * size + "\n", end="")
