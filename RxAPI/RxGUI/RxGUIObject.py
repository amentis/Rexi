__author__ = 'amentis'
from RxAPI import RxObject


class RxGUIObject(RxObject):
    """ The main RxGUI class. Used as a superclass for all RxGUI classes"""
    def __init__(self, name, parent):
        """
        @param parent: RxGUIObject parent object
        @param name: str name of the REXI object
        """
        RxObject.__init__(self, name)
        self._parent = parent
        self.__children = list()

    def get_children(self):
        """
        get a list of the children of the REXI GUI object. Children are of type RxGUIObject.
        @return : list list of child objects
        """
        return self.__children

    def add_child(self, child):
        """
        append a RxGUIObject to the Children list.
        @param child: RxGUIObject
        """
        self.__children.append(child)

    def delete_child(self, child):
        """
        remove a child from the Children list.
        @param child: RxGUIObject child to be removed
        @return: bool True if a child is found and removed, False on fail.
        """
        for i in range(0, len(self.__children)):
            if self.__children[i] == child:
                self.__children.remove(i)
                return True
            return False