#!/usr/bin/python3
"""docstring for Square"""


class Square:
    """docstring for init"""
    def __init__(self, size=0):
        self.size = size
    """size getter method"""
    @property
    def size(self):
        return self.__size
    """size setter method"""
    @size.setter
    def size(self, value):
        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
    """calculate the area of square"""
    def area(self):
        return (self.size ** 2)
    """hastag of squares by size given"""
    def my_print(self):
        # print(self.size)
        if self.size == 0:
            print("")
        elif self.size > 0:
            for i in range(self.size):
                print("#" * self.size)
