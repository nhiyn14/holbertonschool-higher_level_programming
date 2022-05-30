#!/usr/bin/python3
"""
func to check if object is an inheritance of a specific class
"""


def inherits_from(obj, a_class):
    """True if obj is inheritance of a_class, otherwise False"""
    return (isinstance(obj, a_class) and type(obj) != a_class)
