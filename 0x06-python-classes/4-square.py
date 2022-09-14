#!/usr/bin/python3
"""docstring for Square"""


class Square:
    """docstring for init"""
    def __init__(self, size=0):
        self.__size = size
        """size getter method """
    @property
    def size(self):
        return self.__size
    """size setter method"""
    @size.setter
    def size(self, value):
        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an interger")
        elif value < 0:
            raise ValueError("size must be >= 0")
    """claculate the area of sqaure"""
    def area(self):
        return (self.__size ** 2)
