#!/usr/bin/python3
"""
Module to return sum of 2 int

Argument: a, b
"""


def add_integer(a, b=98):
    """My addition function
    Returns: a + b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
