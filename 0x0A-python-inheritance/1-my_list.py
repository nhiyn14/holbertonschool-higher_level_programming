#!/usr/bin/python3
"""
a class MyList that inherits from list
"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """Create instance"""
        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
