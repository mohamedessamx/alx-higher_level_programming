#!/usr/bin/python3
"""
This module contains the Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, which is a special type of rectangle
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class
        Args:
            size (int): The size of the square's sides
        """
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the square
        Returns:
            The area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square
        Returns:
            A string representation of the square in the format [Square] <width>/<height>
        """
        return f"[Square] {self.__size}/{self.__size}"
