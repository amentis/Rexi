__author__ = 'amentis'
from RxAPI.RxGUI import RxGUIObject, RxDynamic


class Screen(RxGUIObject, RxDynamic):

    def __init__(self, title, body=""):
        """
                @type self: str
                ( HTML 5 )
                @type title: str
                ( Page title )
                @type body: str
                ( HTML 5 )
                The main holder for GUI elements. Represents the entire HTML body
                """
        RxGUIObject.__init__(self, "screen", None)
        RxDynamic.__init__(self)
        self.__css = ""
        self.__title = title
        self.__body = body

    def get(self):
        """
        @rtype: str
        @return: Complete HTML 5 page
        """
        for element in self.get_children():
            self.__body += element.get()
        return """<!DOCTYPE HTML>
        <html>
        <head>
        <title> %s</title>
        <script> window.onload = function() {
        %s
        }</script>
        <style> %s </style>
        </head>
        <body> %s </body>
        </html>
        """ % (self.__title, self._javascript, self.__css, self.__body)

    def get_title(self):
        """
        Gets the title of the Screen object
        @return : Page title
        @rtype : str
        """
        return self.__title

    def set_title(self, title):
        """
        Sets the title of the Screen object
        @param title: str
        page title
        """
        self.__title = title

    def get_css(self):
        """
        Gets the current CSS appended to this Screen
        @rtype: str
        @return: CSS, complete CSS of the page
        """
        return self.__css

    def add_css(self, css):
        """
        Appends CSS to this Screen
        @type self: str
        proper CSS
        """
        self.__css += css

    def get_body(self):
        """
        Gets the Body content of the Screen
        @rtype: str
        @return: HTML body content
        """
        return self.__body

    def set_background_color(self, color):
        """
        Sets the background color of the Screen
        @param color: Color
        """
        self.__css += """
        html body {background-color: %s ;}
                """ % color.get()