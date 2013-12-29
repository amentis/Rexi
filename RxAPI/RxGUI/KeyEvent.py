__author__ = 'amentis'
from RxAPI.RxGUI import Event


class KeyEvent(Event):
    def __init__(self, screen, key_name, functions, event_type="keypress", modifiers=""):
        """
        @param screen: Screen
        @param key_name: str
        @param functions: dict
        @param modifiers: str
        @param event_type: str
        """
        Event.__init__(self, screen, modifiers, functions, event_type)
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
        @param key_name: str
        """
        self._key = self.__key_numbers[key_name]

    def get(self):
        functions = ""
        for s in self._functions.values():
            functions += s
        self._javascript = """
        $("#%s").%s(function(event){
                if (event.which == %d) {
                    event.preventDefault();
                    %s
                }
            }
        )
                """ % (self._sender, self._type, self._key, functions)

        return self._javascript