__author__ = 'amentis'
from RxAPI.RxGUI import Event


class KeyEvent(Event):
    def __init__(self, button_name, modifiers, functions, event_type):
        """
        @param button_name: str
        @param modifiers: str
        @param functions: dict
        @param event_type: str
        """
        Event.__init__(self, modifiers, functions, event_type)
        self.__button_numbers = dict
        self.__button_numbers['left'] = 1
        self.__button_numbers['middle'] = 2
        self.__button_numbers['right'] = 3
        self._button = self.__button_numbers[button_name]

    def set_button(self, button_name):
        self._button = self.__button_numbers[button_name]