__author__ = 'amentis'

from RxAPI.RxGUI import *


class Login(Screen):
    """
    Login form for users to enter REXI
    """

    def __init__(self):
        Screen.__init__(self, "REXI Login")
        self.window = Window(self, "Login window")
        self.window.set_size('800px', '600px')
        self.title = Label(self.window, "REXI")
        self.subtitle = Label(self.window, "Remote-accessed Environment-independent eXecuting Interface")
        self.login_form = Window(self.window, "Login form")
        self.username_label = Label(self.login_form, "Username: ")
        self.username_field = LineEdit(self.login_form, "username", "username")
        self.password_label = Label(self.login_form, "Password: ")
        self.password_field = PasswordEdit(self.login_form, "password", "password")
        self.submit_button = Button(self.login_form, "LogIn", "Log In")
        self.set_background_color(Color("screenBackgroundColor", "Lavender"))
        self.window.center()
        self.subtitle.set_size('100%', '200px')