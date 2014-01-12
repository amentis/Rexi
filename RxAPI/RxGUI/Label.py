__author__ = 'amentis'

from RxAPI.RxGUI import RxGUIObject, RxDynamic, Font, Color, Border


class Label(RxGUIObject, RxDynamic):
    """
    label object containing simple text
    """

    def __init__(self, parent, name, text=None):
        """
        @param parent: RxGUIObject parent object
        @param name: str name of the REXI object
        @param text: str text to be shown in the label
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
        set size of the label
        @param width: str width of the label object
        @param height: str height of the label object
        """
        self.__height = height
        self.__width = width

    def set_font(self, font):
        """
        set the font of the text in the label
        @param font: Font
        """
        self.__font = font

    def set_text_color(self, color):
        """
        set the color of the text in the label
        @param color: Color
        """
        self.__text_color = color

    def set_background_color(self, color):
        """
        set the background color of the label
        @param color: Color
        """
        self.__background_color = color

    def set_border(self, border):
        """
        set border for the label object
        @param border: Border
        """
        self.__border = border

    def get_border(self):
        """
        @return: Border label border
        """
        return self.__border

    def set_text(self, text):
        """
        sets the text to be shown in the label
        @param text: str
        """
        self.__text = text

    def get_size(self):
        """
        @return : list list of the label's width as str and height as str
        """
        return [self.__width, self.__height]

    def get_font(self):
        """
        @return : Font the font used for displaying text in the label
        """
        return self.__font

    def get_colors(self):
        """
        @return: list list of text color as Color and background color as Color
        """
        return [self.__text_color, self.__background_color]

    def get_text(self):
        """
        @return : str text displayed in the label
        """
        return self.__text

    def append_text(self, text):
        """
        add text after the end of the text in the label
        @param text: text to be added to the end of the label
        """
        self.__text += text

    def prepend_text(self, text):
        """
        add text before the text in the label
        @param text: text to be added to the beginning of the label
        """
        self.__text = text + self.__text

    def clear_text(self):
        """
        erase all text in the label
        """
        self.__text = ""

    def get_width(self):
        """
        @return: str width of the label
        """
        return self.__width

    def get_height(self):
        """
        @return: str height of the label
        """
        return self.__height

    def get(self):
        """
        @return: str  HTML code of the label
        """
        self._parent.add_css(self.__css)
        self._parent.append_javascript(self.get_javascript())
        return """
        <span id=\"%s\" class=\"label\"> %s </span>
            """ % (self.get_name(), self.get_text())