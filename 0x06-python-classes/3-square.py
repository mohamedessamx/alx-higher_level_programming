#!/usr/bin/python3

class square:
    """define a square."""

    def __init__(self, size=0):
        """constructor.

        args:
            size:length of a side of the square.
        Raises:
            TyprError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of this square.

        Return:
            this size squared
        """
        return self.__size ** 2
