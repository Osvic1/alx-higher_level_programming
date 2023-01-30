#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """
    Defines a rectangle by setting its width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        Raises a TypeError if the width is not an integer.
        Raises a ValueError if the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        Raises a TypeError if the height is not an integer.
        Raises a ValueError if the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
