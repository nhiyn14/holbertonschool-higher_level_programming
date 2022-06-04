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

    def update(self, *args, **kwargs):
        """assigns a key/value argument to each attribute"""
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dictSq = {}
        dictSq["id"] = self.id
        dictSq["size"] = self.size
        dictSq["x"] = self.x
        dictSq["y"] = self.y
        return dictSq
