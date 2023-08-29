#!/usr/bin/python3
""" define class, Square """


class Square:
    """ shared between all of the class instances
    Attributes:
    __size (int): the square side size
    """
    def __init__(self, size=0):
        """ class initialization, passing initial values to object
        Args:
            size (init): square side size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ public instance, returns the current square area """
        return self.__size ** 2
