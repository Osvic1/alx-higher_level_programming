#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    This class represents a basic geometry object with implementation for
    integer validation.
    """
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value passed to it.

        Args:
        1. name: A string representing the name of the value
        2. value: An integer that needs to be validated

        Raises:
        1. TypeError: If the value passed is not an integer
        2. ValueError: If the value passed is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
