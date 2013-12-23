__author__ = 'amentis'


class RxObject:
    """ The main RxApi class. Used as superclass for all other classes """

    def __init__(self, name):
        """
        @param name: str
        """
        self.__name = name

    def get_name(self):
        """
        Sets a name for the REXI object
        @return: str
        """
        return self.__name

    def set_name(self, name):
        """
        Gets the name of a REXI object
        @param name: str
        RxObject name
        """
        self.__name = name