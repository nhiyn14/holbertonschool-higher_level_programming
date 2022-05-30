#!/usr/bin/python3
"""
func to check if object is an instance of a specific class
"""


def is_same_class(obj, a_class):
    """True if obj is instance of a_class, otherwise False"""
    return (type(obj) == a_class)
