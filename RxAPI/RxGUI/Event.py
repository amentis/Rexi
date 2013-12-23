__author__ = 'amentis'
from RxAPI.RxGUI import RxDynamic


class Event(RxDynamic):
    def __init__(self, modifiers, functions, event_type):
        """
        @param modifiers: list
        @param functions: dict
        """
        RxDynamic.__init__(RxDynamic(self))
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
        self._sender = ""
        self._target = ""
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

    def set_target(self, target):
        """
        @param target: str
        """
        self._target = target

    def get_target(self):
        """
        @rtype : str
        """
        return self._target

    def set_connection(self, sender, target):
        """
        @param sender: str
        @param target: str
        """
        self._sender = sender
        self._target = target

    def get_connection(self):
        """
        @rtype : list
        """
        return [self._sender, self._target]

    def add_function(self, name, function):
        """
        @param name: str
        @param function: str
        """
        self._functions[name] = function

    def get_function(self, name):
        """
        @rtype : str
        """
        return self._functions[name]

    def get_all_functions(self):
        """
        @rtype : list
        """
        return self._functions.values

    def remove_function(self, name):
        """
        @param name: str
        """
        self._functions.pop(name)

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