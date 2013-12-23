__author__ = 'amentis'
from RxAPI import RxObject


class RxGUIObject(RxObject):
    """ The main RxGUI class. Used as a superclass for all RxGUI classes"""
    def __init__(self, name, parent):
        """
        @param name: str
        @param parent: RxGUIObject
        """
        RxObject.__init__(self, name)
        self._parent = parent
        self.__children = list()

    def get_children(self):
        """
        Gets a list of the children of the RxGUI object. Children are of type RxGUIObject.
        @rtype : list
        @return : list of child objects
        """
        return self.__children

    def add_child(self, child):
        """
        Appends a RxGUIObject to the Children list.
        @param child: RxGUIObject
        """
        self.__children.append(child)

    def delete_child(self, child):
        """
        Removes a child from the Children list.
        @param child: RxGUIObject
        @return: True if a child is found and removed, False on fail.
        @rtype: bool
        """
        for i in range(0, len(self.__children)):
            if self.__children[i] == child:
                self.__children.remove(i)
                return True
            return False