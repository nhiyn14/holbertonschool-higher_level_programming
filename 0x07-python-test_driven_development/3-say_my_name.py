#!/usr/bin/python3
"""Module to print first and last name
"""


def say_my_name(first_name, last_name=""):
    """function that prints full name
    Returns: My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    return print(f"My name is {first_name} {last_name}")
