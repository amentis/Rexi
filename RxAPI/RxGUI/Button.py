__author__ = 'amentis'
from RxAPI.RxGUI import RxGUIObject, RxDynamic
from RxAPI import RxObject


class Button(RxGUIObject, RxDynamic):
    def __init__(self, parent, name):
        RxGUIObject.__init__(self, name, parent)
        RxDynamic.__init__(RxObject(self))
        pass