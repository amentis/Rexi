__author__ = 'amentis'
from RxAPI.RxGUI import RxGUIObject, RxDynamic
from RxAPI import RxObject


class Event(RxDynamic, RxGUIObject):
    def __init__(self, parent, sender, modifiers, functions, event_type):
        """
        @param parent: RxGUIObject
        @param modifiers: list
        @param functions: list
        @param event_type: str
        """
        RxGUIObject.__init__(self, "__event__", parent)
        RxDynamic.__init__(RxObject(self))
        self._parent.add_child(self)
        if "alt" in modifiers:
            self._alt = True
        else:
            self._alt = False
        if "shift" in modifiers:
            self._shift = True
        else:
            self._shift = False
        if "ctrl" in modifiers:
            self._ctrl = True
        else:
            self._ctrl = False
        self._functions = functions
        self._sender = sender
        self._type = event_type

    def set_sender(self, sender):
        """
        @param sender: str
        """
        self._sender = sender

    def get_sender(self):
        """
        @rtype : str
        """
        return self._sender

    def add_function(self, function):
        """
        @param function: str
        """
        self._functions.append(function)

    def get_function(self, number):
        """
        @rtype : int
        """
        return self._functions[number]

    def get_all_functions(self):
        """
        @rtype : list
        """
        return self._functions

    def remove_function(self, number):
        """
        @param number: int
        """
        self._functions.pop(number)

    def remove_all_functions(self):
        self._functions.clear()

    def get_modifiers(self):
        """
        @rtype : str
        """
        return u"ctrl: {0:s}, alt: {1:s}, shift: {2:s}".format(self._ctrl, self._alt, self._shift)

    def set_modifiers(self, modifiers):
        """
        @param modifiers: str
        """
        if "alt" in modifiers:
            self._alt = True
        else:
            self._alt = False
        if "shift" in modifiers:
            self._shift = True
        else:
            self._shift = False
        if "ctrl" in modifiers:
            self._ctrl = True
        else:
            self._ctrl = False