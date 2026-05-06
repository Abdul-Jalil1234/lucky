#!/usr/bin/python3
"""
This module defines a Square class with size validation.
"""


class Square:
    """
    Defines a square with validation for size.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size=0):
        """
        Initializes the square with size validation.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
