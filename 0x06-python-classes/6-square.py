#!/usr/bin/python3
"""Create a class with Public instance methods"""


class Square:
    """Defines a square

    Attributes:
        __size (int): Square size
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property to retrieve __size

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for __size

        Args:
            value (int): Square size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        """Make value Private instance attribute size

        Args:
            __size (int): Square size
        """
        self.__size = value

    @property
    def position(self):
        """Property to retrieve __position

        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for __position

        Args:
            value (int): Square position
        """
        err = "position must be a tuple of 2 positive integers"
        if len(value) != 2:
            raise TypeError(err)
        if type(value) is not tuple:
            raise TypeError(err)
        else:
            if value[0] < 0 or value[1] < 0:
                    raise TypeError(err)

        """Make value Private instance attribute size

        Args:
            __size (int): Square size
        """
        self.__position = value

    def area(self):
        """Public instance method 'area'

        Return: current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout the square with the character #

        Return: Square of #
        """
        if self.__size != 0:
            for row in range(self.size):
                for col in range(self.position[0]):
                    print(" ", end="")
                for col in range(self.size):
                    print("#", end="")
                print()
        else:
            print()
