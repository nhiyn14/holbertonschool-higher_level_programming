#!/usr/bin/python3
"""
a class MyInt that inherits from int
"""


class MyInt(int):
    """subclass of Int where == and != operators inverted"""
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
