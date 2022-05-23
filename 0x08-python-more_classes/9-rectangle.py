#!/usr/bin/python3
"""Create class Rectangle with Private attribute: width and height"""


class Rectangle:
    """Define Rectangle

    Attributes:
        width: Width of Rectangle
        height: Height of Rectangle
        number_of_instances: instance count
        print_symbol: symbol to print rectangle with
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init instance with class Rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter property to retrive __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter property for __width to value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter property to retrive __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter property for __height to value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ print the rectangle with the character #"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                string += str(self.print_symbol) * self.__width
                if i != self.height - 1:
                    string += "\n"
        return string

    def __repr__(self):
        """return a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print "Bye rectangle..." when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
