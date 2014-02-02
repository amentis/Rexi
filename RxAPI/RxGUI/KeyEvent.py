__author__ = 'amentis'
from RxAPI.RxGUI import Event


class KeyEvent(Event):
    """
    definition for an event, being called upon keyboard event
    """
    def __init__(self, parent, sender, key_name, actions, event_type="keypress", modifiers=""):
        """
        @param parent: RxGUIObject parent object
        @param sender: str name of the object sending the event
        @param key_name: name of the keyboard key. Acceptable values:
        'Backspace', 'Tab', 'Enter', 'Shift', 'Ctrl', 'Alt', 'PauseBreak', 'CapsLock', 'Esc', 'PageUp',
        'PageDown', 'End', 'Home', 'Left', 'Up', 'Right', 'Down', 'Insert', 'Delete', '0', '1', '2', '3', '4',
        '5', '6', '7', '8', '9', 'colon', 'equals', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Meta', 'Super', 'Win', 'RightClick',
        'Num0', 'Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6', 'Num7', 'Num8', 'Num9', 'Num*', 'Num+', 'Num-',
        'Num.', 'Num/', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'NumLock',
        ScrollLock', ',', '.', '/', '`', '[', ']', '/', '"'
        @param actions: list list of str, methods to be called on this event
        @param modifiers: list list of str, keyboard modifiers (alt, shift and/or ctrl)
        @param event_type: str type of event. Acceptable values: keydown, keypress, keyup
        """
        Event.__init__(self, parent, sender, modifiers, actions, event_type)
        self.__key_numbers = dict()

        self.__key_numbers['Backspace'] = 8
        self.__key_numbers['Tab'] = 9
        self.__key_numbers['Enter'] = 13
        self.__key_numbers['Shift'] = 16
        self.__key_numbers['Ctrl'] = 17
        self.__key_numbers['Alt'] = 18
        self.__key_numbers['PauseBreak'] = 19
        self.__key_numbers['CapsLock'] = 20
        self.__key_numbers['Esc'] = 27
        self.__key_numbers['PageUp'] = 33
        self.__key_numbers['PageDown'] = 34
        self.__key_numbers['End'] = 35
        self.__key_numbers['Home'] = 36
        self.__key_numbers['Left'] = 37
        self.__key_numbers['Up'] = 38
        self.__key_numbers['Right'] = 39
        self.__key_numbers['Down'] = 40
        self.__key_numbers['Insert'] = 45
        self.__key_numbers['Delete'] = 46
        self.__key_numbers['0'] = 48
        self.__key_numbers['1'] = 49
        self.__key_numbers['2'] = 50
        self.__key_numbers['3'] = 51
        self.__key_numbers['4'] = 52
        self.__key_numbers['5'] = 53
        self.__key_numbers['6'] = 54
        self.__key_numbers['7'] = 55
        self.__key_numbers['8'] = 56
        self.__key_numbers['9'] = 57
        self.__key_numbers['colon'] = 59
        self.__key_numbers['equals'] = 61
        self.__key_numbers['a'] = 65
        self.__key_numbers['b'] = 66
        self.__key_numbers['c'] = 67
        self.__key_numbers['d'] = 68
        self.__key_numbers['e'] = 69
        self.__key_numbers['f'] = 70
        self.__key_numbers['g'] = 71
        self.__key_numbers['h'] = 72
        self.__key_numbers['i'] = 73
        self.__key_numbers['j'] = 74
        self.__key_numbers['k'] = 75
        self.__key_numbers['l'] = 76
        self.__key_numbers['m'] = 77
        self.__key_numbers['n'] = 78
        self.__key_numbers['o'] = 79
        self.__key_numbers['p'] = 80
        self.__key_numbers['q'] = 81
        self.__key_numbers['r'] = 82
        self.__key_numbers['s'] = 83
        self.__key_numbers['t'] = 84
        self.__key_numbers['u'] = 85
        self.__key_numbers['v'] = 86
        self.__key_numbers['w'] = 87
        self.__key_numbers['x'] = 88
        self.__key_numbers['y'] = 89
        self.__key_numbers['z'] = 90
        self.__key_numbers['Meta'] = 91
        self.__key_numbers['Super'] = 91
        self.__key_numbers['Win'] = 91
        self.__key_numbers['RightClick'] = 93
        self.__key_numbers['Num0'] = 96
        self.__key_numbers['Num1'] = 97
        self.__key_numbers['Num2'] = 98
        self.__key_numbers['Num3'] = 99
        self.__key_numbers['Num4'] = 100
        self.__key_numbers['Num5'] = 101
        self.__key_numbers['Num6'] = 102
        self.__key_numbers['Num7'] = 103
        self.__key_numbers['Num8'] = 104
        self.__key_numbers['Num9'] = 105
        self.__key_numbers['Num*'] = 106
        self.__key_numbers['Num+'] = 107
        self.__key_numbers['Num-'] = 109
        self.__key_numbers['Num.'] = 110
        self.__key_numbers['Num/'] = 111
        self.__key_numbers['F1'] = 112
        self.__key_numbers['F2'] = 113
        self.__key_numbers['F3'] = 114
        self.__key_numbers['F4'] = 115
        self.__key_numbers['F5'] = 116
        self.__key_numbers['F6'] = 117
        self.__key_numbers['F7'] = 118
        self.__key_numbers['F8'] = 119
        self.__key_numbers['F9'] = 120
        self.__key_numbers['F10'] = 121
        self.__key_numbers['F11'] = 122
        self.__key_numbers['F12'] = 123
        self.__key_numbers['NumLock'] = 144
        self.__key_numbers['ScrollLock'] = 145
        self.__key_numbers[','] = 188
        self.__key_numbers['.'] = 190
        self.__key_numbers['/'] = 191
        self.__key_numbers['`'] = 192
        self.__key_numbers['['] = 219
        self.__key_numbers[']'] = 221
        self.__key_numbers['/'] = 220
        self.__key_numbers['"'] = 220

        self._key = self.__key_numbers[key_name]

    def set_key(self, key_name):
        """
        set the key which triggers the event
        @param key_name: name of the keyboard key. Acceptable values:
        'Backspace', 'Tab', 'Enter', 'Shift', 'Ctrl', 'Alt', 'PauseBreak', 'CapsLock', 'Esc', 'PageUp',
        'PageDown', 'End', 'Home', 'Left', 'Up', 'Right', 'Down', 'Insert', 'Delete', '0', '1', '2', '3', '4',
        '5', '6', '7', '8', '9', 'colon', 'equals', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Meta', 'Super', 'Win', 'RightClick',
        'Num0', 'Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6', 'Num7', 'Num8', 'Num9', 'Num*', 'Num+', 'Num-',
        'Num.', 'Num/', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'NumLock',
        ScrollLock', ',', '.', '/', '`', '[', ']', '/', '"'
        """
        self._key = self.__key_numbers[key_name]

    def get(self):
        """
        setup the key event
        """
        functions = ""
        for s in self._actions:
            functions += s + "; \n"
        self._javascript = """
        $("#%s").%s(function(event){
                if (event.which == %d) {
                    event.preventDefault();
                    %s
                }
            }
        )
                """ % (self._sender, self._type, self._key, functions)

        self._parent.append_javascript(self._javascript)

        return ""