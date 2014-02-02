__author__ = 'amentis'
import sys
from RxAPI import RxObject


class RxDynamic(RxObject):
    """
    Wrapper for dynamic (JavaScript - dependent) REXI classes
    """

    def __init__(self):
        self._javascript = ""
        for element in sys.modules.keys():
            if element.split(".")[0] == "RxAPI":
                try:
                    if not sys.modules.get(element).javascript_class in self._parent.get_javascript():
                        self._javascript += sys.modules.get(element).javascript_class + "\n"
                except AttributeError:
                    pass

    def append_javascript(self, javascript):
        self._javascript += javascript

    def get_javascript(self):
        return self._javascript