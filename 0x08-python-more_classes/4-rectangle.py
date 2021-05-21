#!/usr/bin/python3
'Rectangle'


class Rectangle:
    'class defines a rectangle'
    def __init__(self, width=0, height=0):
        'starts our rectangle with default values'
        self.width = width
        self.height = height

    def area(self):
        'returns the area of the rectangle'
        a = self.__width * self.__height
        return(a)

    def perimeter(self):
        'returns the perimeter of the rectangle'
        if self.__width == 0 or self.height == 0:
            p = 0
        else:
            p = (self.__width * 2) + (self.__height * 2)
        return(p)

    def __str__(self):
        'returns a rectangle-shaped string according to its size'
        s = ""
        if self.__width == 0 or self.__height == 0:
            return(s)
        else:
            l = 1
            for i in range(self.__height):
                for j in range(self.__width):
                    s = s + '#'
                if l < self.__height:
                    s = s + '\n'
                    l += 1
            return(s)

    def __repr__(self):
        'return a string representation of the rectangle'
        r = "Rectangle({}, {})".format(self.__width, self.__height)
        return(r)

    @property
    def width(self):
        'returns the width value of the rectangle'
        return(self.__width)

    @width.setter
    def width(self, value):
        'validates type of data and the size of the width of the rectangle'
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        'returns the height value of the rectangle'
        return(self.__height)

    @height.setter
    def height(self, value):
        'validates type of data and the size of the height of the rectangle'
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
