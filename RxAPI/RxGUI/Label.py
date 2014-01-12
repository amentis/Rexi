__author__ = 'amentis'

from RxAPI.RxGUI import RxGUIObject, RxDynamic, Font, Color, Border


class Label(RxGUIObject, RxDynamic):
    def __init__(self, parent, name, text=None):
        """
        @param parent: RxGUIObject
        @param name: str
        @param text: str
        """
        RxGUIObject.__init__(self, name, parent)
        RxDynamic.__init__(self)
        if not text:
            text = name
        self.__text = text
        self.__height = ''
        self.__width = ''
        self.__font = Font(self, "font")
        self.__text_color = Color("textColor")
        self.__background_color = Color("backgroundColor")
        self.__border = Border(self, "border")
        self._parent.add_child(self)
        self.__css = ""

    def set_size(self, width, height):
        """
        @param width: str
        @param height: str
        """
        self.__height = height
        self.__width = width

    def set_font(self, font):
        """

        @param font: Font
        """
        self.__font = font

    def set_text_color(self, color):
        """

        @param color: Color
        """
        self.__text_color = color

    def set_background_color(self, color):
        """

        @param color: Color
        """
        self.__background_color = color

    def set_border(self, border):
        """

        @param border: Border
        """
        self.__border = border

    def get_border(self):
        """


        @return: Border
        """
        return self.__border

    def set_text(self, text):
        """

        @param text: str
        """
        self.__text = text

    def get_size(self):
        """

        @rtype : list
        @return : list of width as str and height as str
        """
        return [self.__width, self.__height]

    def get_font(self):
        """

        @rtype : Font
        """
        return self.__font

    def get_colors(self):
        """

        @rtype: list
        @return: list of text color as Color and background color as Color
        """
        return [self.__text_color, self.__background_color]

    def get_text(self):
        """

        @rtype : str
        """
        return self.__text

    def append_text(self, text):
        self.__text += text

    def prepend_text(self, text):
        self.__text = text + self.__text

    def clear_text(self):
        self.__text = ""

    def get_width(self):
        """


        @return: str
        """
        return self.__width

    def get_height(self):
        """


        @return: str
        """
        return self.__height

    def get(self):
        """
        @return: str
        """
        self._parent.add_css(self.__css)
        self._parent.append_javascript(self.get_javascript())
        return """
        <span id=\"%s\" class=\"label\"> %s </span>
            """ % (self.get_name(), self.get_text())