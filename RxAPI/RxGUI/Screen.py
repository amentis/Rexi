__author__ = 'amentis'
from RxAPI.RxGUI import RxGUIObject, RxDynamic


class Screen(RxGUIObject, RxDynamic):
    """
    The main holder for GUI elements. Represents the entire HTML body
    """

    def __init__(self, title, body=""):
        """
        @param title: str Page __title
        @param body: str HTML body
        """
        RxGUIObject.__init__(self, "screen", None)
        RxDynamic.__init__(self)
        self.__css = ""
        self.__title = title
        self.__body = body

    def get(self):
        """
        @return: str complete HTML 5 page
        """
        for element in self.get_children():
            self.__body += element.get()
        return """<!DOCTYPE HTML>
        <html>
        <head>
        <title> %s</title>
        <script src="jquery-2.0.3.min.js"></script>
        <script> $(document).ready(function(){
        %s
        });</script>
        <style> %s </style>
        </head>
        <body> %s </body>
        </html>
        """ % (self.__title, self._javascript, self.__css, self.__body)

    def get_title(self):
        """
        @return : str page __title
        """
        return self.__title

    def set_title(self, title):
        """
        set the __title of the Screen object - page
        @param title: str page __title
        """
        self.__title = title

    def get_css(self):
        """
        get the current CSS appended to this Screen
        @return: str complete code CSS of the page
        """
        return self.__css

    def add_css(self, css):
        """
        append CSS to this Screen
        @param css: str CSS to be appended
        """
        self.__css += css

    def get_body(self):
        """
        @return: str HTML body content
        """
        return self.__body

    def set_background_color(self, color):
        """
        set the background color of the Screen
        @param color: Color
        """
        self.__css += """
        html body {background-color: %s ;}
                """ % color.get()