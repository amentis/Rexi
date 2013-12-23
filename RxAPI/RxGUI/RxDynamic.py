__author__ = 'amentis'
import sys
from RxAPI import RxObject


class RxDynamic(RxObject):
    """ Wrapper for dynamic (JavaScript - dependent) REXI classes """

    def __init__(self):
        self._javascript = ""
        for element in sys.modules.keys():
            if element.split(".")[0] == "RxAPI":
                try:
                    if not sys.modules.get(element).javascript_class in self._parent.get_javascript():
                        self._javascript += sys.modules.get(element).javascript_class + "\n"
                except AttributeError:
                    pass

    def connect(self, event, receiver, method, key=None):
        """
        @param event str
        Mouse: onClick, onDblClick, onMouseDown, onMouseMove, onMouseOver, onMouseOut, onMouseUp,
        Keyboard: onKeyDown, onKeyPress onKeyUp,
        Frame/Object: onAbort, onError, onLoad, onResize, onScroll, onUnload,
        Form: onBlur, onChange, onFocus, onReset, onSelect, onSubmit
        @param receiver str
        receiver object name
        @param method str
        receiver object method
        """
        if not key:
            self._javascript += """$(\"#%s\").%s = %s.%s;""" % (
                self.get_name(), event, receiver, method)
        else:
            self._javascript += """
            $(\"#%s\").%s(function (event) {
                if (event.which == %d || event.keyCode == %d) {
                    event.preventDefault();
                    %s.%s;
                }
            });
            """ % (self.get_name(), event, key, key, receiver, method)

    def append_javascript(self, javascript):
        self._javascript += javascript

    def get_javascript(self):
        return self._javascript