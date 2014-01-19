__author__ = 'amentis'
from RxAPI.RxGUI import StylableObject, RxDynamic


class Window(StylableObject, RxDynamic):
    """
    an element holder to organize elements
    """
    def __init__(self, parent, name):
        """
        @param parent: RxGUIObject parent object
        @param name: str name of the REXI object
        """
        StylableObject.__init__(self, name, parent)
        RxDynamic.__init__(self)
        self.__body = ""
        self.__css = ""
        self._parent.add_child(self)

    def get(self):
        """
        @return: str HTML code of the Window
        """
        for element in self.get_children():
            self.__body += element.get()
        self._parent.append_javascript(self.get_javascript())
        self._parent.add_css(self.get_css())

        return """
        <div id="{0}">
        {1}
        </div>""".format(self.get_name(), self.__body)

    def get_body(self):
        """
        @return: str HTML body of the window
        """
        return self.__body

    def get_css(self):
        """
        @return: str CSS of the Window
        """
        return self.__css

    def add_css(self, css):
        """
        add CSS code to the window object
        @param css: str CSS code to be appended
        """
        self.__css += css

    def center(self):
        """
        orient all the elements in the window to the center
        """
        self.__css += "#%s {margin-left: auto; margin-right: auto;}" % self.get_name()