#!/usr/bin/python3
"""
This module contains a class that inherits from the list type.
It allows for the creation of lists that can exclude specific elements.
"""


class MyList(list):
    """
    This class provides a specialized list with custom behavior.
    It maintains all the standard functionality of a Python list.
    """

    def print_sorted(self):
        """
        This method displays the elements of the list in ascending order.
        The original list remains unchanged after this operation.
        """
        print(sorted(self))
