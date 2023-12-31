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
        self.__size = size

    def area(self):
        """ public instance, returns the current square area """
        return self.__size ** 2

    @property
    def size(self):
        """ method gets object size value

        Returns:
        int: object size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ method functions as the setter
        Args:
                    size (init): square side size
        """
        self.__size = size

    def area(self):
        """ public instance, returns the current square area """
        return self.__size ** 2

    @property
    def size(self):
        """ method gets object size value

        Returns:
        int: object size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ method functions as the setter
        Args:
        Value (int): new size value to be set

        Raises:
        TypeError: if the value provided is not  an integer type
        ValueError: if the value provided is < 0 """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ prints square with # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
