#!/usr/bin/python3
"""
Class Rectangle that inherits from Base
"""

from models.base import Base

class Rectangle(Base):
    """Class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init an instance"""
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter property to retrieve __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter property for __width to value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter property to retrieve __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter property for __height to value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter property to retrieve __x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter property for __x to value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter property to retrieve __y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter property for __y to value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the Rectangle area"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance of #"""
        for i in range(self.__height):
            print('#' * self.__width)
