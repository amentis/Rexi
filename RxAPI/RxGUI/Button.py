__author__ = 'amentis'
from RxAPI.RxGUI import StylableObject, RxDynamic
from RxAPI import RxObject


class Button(StylableObject, RxDynamic):
    def __init__(self, parent, name):
        StylableObject.__init__(self, name, parent)
        RxDynamic.__init__(RxObject(self))
        pass