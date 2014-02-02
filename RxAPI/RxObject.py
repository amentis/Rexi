__author__ = 'amentis'


class RxObject:
    """
    The main RxApi class. Used as superclass for all other classes
    """

    def __init__(self, name):
        """
        @param name: str name of the object
        """
        self.__name = name

    def get_name(self):
        """
        @return: str name of the REXI object
        """
        return self.__name

    def set_name(self, name):
        """
        sets the name of the REXI object
        @param name: str name of the object
        """
        self.__name = name