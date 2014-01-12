__author__ = 'amentis'
from RxAPI.RxGUI import Event


class MouseEvent(Event):
    def __init__(self, parent, sender, button_name, modifiers, actions, event_type="click"):
        """
        @param parent: RxGUIObject parent object
        @param sender: str name of the object sending the event
        @param button_name: str name of the mouse button. Acceptable values: left, middle, right
        @param actions: list list of str, methods to be called on this event
        @param modifiers: list list of str, keyboard modifiers (alt, shift and/or ctrl)
        @param event_type: str type of event. Acceptable values:
        """
        Event.__init__(self, parent, sender, modifiers, actions, event_type)
        self.__button_numbers = dict
        self.__button_numbers['left'] = 1
        self.__button_numbers['middle'] = 2
        self.__button_numbers['right'] = 3
        self._button = self.__button_numbers[button_name]

    def set_button(self, button_name):
        """
        set the button which triggers the event
        @param button_name: str name of the mouse button. Acceptable values: left, middle, right
        """
        self._button = self.__button_numbers[button_name]

    def get(self):
        """
        setup the mouse event
        """
        functions = ""
        for s in self._actions.values:
            functions += s
        self._javascript = """
        $("#%s").%s(function(event){
                if (event.which == %d) {
                    event.preventDefault();
                    %s
                }
            }
        )
                """ % (self._sender, self._type, self._button, functions)