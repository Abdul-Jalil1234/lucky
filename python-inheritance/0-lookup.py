#!/usr/bin/python3
"""
This module contains a utility function for object introspection.
It provides a way to examine the members of any given object.
"""


def lookup(obj):
    """
    This function finds and returns all available attributes and methods.
    The result is a list containing the names of these members as strings.
    """
    return dir(obj)
