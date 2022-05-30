#!/usr/bin/python3
"""
func to check if object is an instance/inheritance of a specific class
"""


def is_kind_of_class(obj, a_class):
    """True if obj is instance/inheritance of a_class, otherwise False"""
    return (isinstance(obj, a_class))
