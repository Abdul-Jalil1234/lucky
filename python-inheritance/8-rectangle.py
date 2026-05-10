#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
It includes specific implementations for area and string representation.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle shape with private dimensions.
    """

    def __init__(self, width, height):
        """
        This method initializes a new Rectangle instance.
        The dimensions are validated before storage.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        This method calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        This method returns a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
