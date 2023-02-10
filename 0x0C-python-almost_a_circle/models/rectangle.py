#!/usr/bin/python3
'''A module for class Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''A class representing a Rectangle.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init_(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            '''width of the rectangle.'''
            return self.__width

        @width.setter
        def width(self, value):
            self.validate_integer("width", value, False)
            self.__width = value

        @property
        def height(self):
            '''Height of the rectangle.'''
            return self.__height

        @height.setter
        def height(self, value):
            self.validate_integer("height", value, False)
            self.__height = value

        @property
        def x(self):
            '''x of this rectangle.'''
            return self.__x

        @x.setter
        def x(self, value):
            self.validate_integer("x", value)
            self.__x = value

        @property
        def y(self):
            '''y of this rectangle.'''
            return self.__y

        @y.setter
        def y(self, value):
            self.validate_integer("y", value)
            self.__y = value

        def validate_interger(self, name, value, eq=True):
            '''method for validating the value of the rectangle.'''
            if type(value) != int:
                raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

        def area(self):
            '''Computes area of this rectangle.'''
            return self.width * self.height

        def display(self):
            '''Prints string representation of this rectangle.'''
            s = '\n' * self.y + \
                (' ' * self.x + '#' * self.width + '\n') * self.height
            print(s, end='')
