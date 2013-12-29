__author__ = 'amentis'

from RxAPI.RxGUI import *


class Login(Screen):
    def __init__(self):
        Screen.__init__(self, "REXI Login")
        self.__window = Window(self, "Login window")
        self.__title = Label(self, "REXI")
        self.__subtitle = Label(self, "Remote-accessed Environment-independent eXecuting Interface")
        self.__login_form = Window(self.__window, "Login form")
