__author__ = 'amentis'
from RxAPI.RxGUI import *


class Console(Screen):

    def __init__(self):
        Screen.__init__(self, "REXI Console")
        self._window = Window(self, 'consoleWindow')
        self._output = TextView(self._window, 'output')
        self._input = TextEdit(self._window, 'input')
        self._window.set_size('800px', '600px')
        self._input.set_size('100%', '10%')
        self._output.set_size('100%', '90%')
        self._screen_bckg_color = Color("screenBackgroundColor")
        self._screen_bckg_color.color_by_name("Lavender")
        self.set_background_color(self._screen_bckg_color)
        self._window.center()
        self._fields_bckg_color = Color("outputBackgroundColor")
        self._fields_bckg_color.color_by_rgba(200, 200, 200, 0.7)
        self._output.set_background_color(self._fields_bckg_color)
        self._input.set_background_color(self._fields_bckg_color)
        self._output.set_border(Border("OutputBorder", Color("OutputBorderColor", "Black")))
        self._input.set_border(Border("InputBorder", Color("InputBorderColor", "Black")))
        self._on_enter = KeyEvent(self, "Enter",
                                  dict(
                                      append="append_text(\"<br>\" + %s.get_text())" % self._input.get_name(),
                                      clear="clear_text()"
                                  ))

    def get(self):
        return Screen.get(self)