#!/usr/bin/python3
"""Define a class square."""


class square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int):length of a side of the square.
        Raises:
            TyprError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
