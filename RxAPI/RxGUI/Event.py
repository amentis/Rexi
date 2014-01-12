__author__ = 'amentis'
from RxAPI.RxGUI import RxGUIObject, RxDynamic
from RxAPI import RxObject


class Event(RxDynamic, RxGUIObject):
    """
    Superclass for different dynamic events
    """

    def __init__(self, parent, sender, modifiers, actions, event_type):
        """
        @param parent: RxGUIObject parent object
        @param modifiers: list list of str, keyboard modifiers (alt, shift and/or ctrl)
        @param actions: list list of str, methods to be called on this event
        @param event_type: str type of event (types defined in children)
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
        self._actions = actions
        self._sender = sender
        self._type = event_type

    def set_sender(self, sender):
        """
        set the sender of the event
        @param sender: str name of the object sending the event
        """
        self._sender = sender

    def get_sender(self):
        """
        @return : str name of the object sending the event
        """
        return self._sender

    def add_action(self, function):
        """
        append action to the list of actions to be done on this event
        @param function: str action - method to be called on this event
        """
        self._actions.append(function)

    def get_action(self, number):
        """
        @param number: int index of the action
        @return : str action in the specified index of the list of actions
        """
        return self._actions[number]

    def get_all_actions(self):
        """
        @return : list list of str, all off the actions in the event object
        """
        return self._actions

    def remove_action(self, number):
        """
        remove the action on this index of the list of actions
        @param number: int index of the action to be removed
        """
        self._actions.pop(number)

    def remove_all_actions(self):
        """
        empty the list of actions
        """
        self._actions.clear()

    def get_modifiers(self):
        """
        @return : str string showing which modifier keys are being used for this event
        """
        return u"ctrl: {0:s}, alt: {1:s}, shift: {2:s}".format(self._ctrl, self._alt, self._shift)

    def set_modifiers(self, modifiers):
        """
        set modifier keys usage in calling this event
        @param modifiers: str string of the modifier keys to be used, separated by spaces
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