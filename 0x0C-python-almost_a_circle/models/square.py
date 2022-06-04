#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
"""

from models.base import Base
from models.rectangle import Rectangle

class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init an instance"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter property to retrieve __size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter property for __size to value"""
        self.width = value
        self.height = value

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <width>/<height>"""
        return (f"[Square] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}")
