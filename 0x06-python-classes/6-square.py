#!/usr/bin/python3
""" define class, Square """


class Square:
    """ shared between all of the class instances
    Attributes:
    __size (int): the square side size
    """
    def __init__(self, size=0, position=(0, 0)):
        """ class initialization, passing initial values to object
        Args:
            size (init): square side size
        """
        self.__size = size
        self.__position = position

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
            print('')
            return

        [print('') for i in range(0, self.__position[1])]
        for i in range(0, self__size):
            [print(' ', end='') for f in range(0, self.__position[0])]
            [print('#', end='') for n in range(0, self_size)]
            print('')
    @property
    def position(self):
        """ gets object position

        Returns: object position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets square position
        Args:
        value as two positive integers tuple
        Raises:
        TypeError: if value is no tuple
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
    self.__position = value
