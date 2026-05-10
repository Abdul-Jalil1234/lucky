#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
It provides specialized area calculations and string formatting.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class represents a square using a single size attribute.
    It utilizes the Rectangle parent class for its foundation.
    """

    def __init__(self, size):
        """
        This method initializes a new Square instance.
        It validates the size and uses the parent constructor.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        This method returns the area of the square instance.
        It calculates the result by squaring the private size.
        """
        return self.__size ** 2

    def __str__(self):
        """
        This method returns a string representation of the square.
        The format displays the class name and the dimensions.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
