__author__ = 'amentis'

from RxAPI.RxGUI import *


class Login(Screen):
    """
    Login form for users to enter REXI
    """

    def __init__(self):
        Screen.__init__(self, "REXI Login")
        self.__window = Window(self, "Login window")
        self.__title = Label(self.__window, "REXI")
        self.__subtitle = Label(self.__window, "Remote-accessed Environment-independent eXecuting Interface")
        self.__login_form = Window(self.__window, "Login form")
        self.__username_label = Label(self.__login_form, "Username: ")
        self.__username_field = LineEdit(self.__login_form, "username", "username")
        self.__password_label = Label(self.__login_form, "Password: ")
        self.__password_field = PasswordEdit(self.__login_form, "password", "password")