#!/usr/bin/python3
""" define class, Square """


class Square:
    """ shared between all of the class instances
    Attributes:
    __size (int): the square side size
    """
    def __init__(self, size):
        """ class initialization, passing initial values to object
        Args:
            size (init): square side size
        Returns: None
        """
        self.__size = size
