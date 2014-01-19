from RxAPI.RxGUI import RxGUIObject, Font, Color, Border

__author__ = 'amentis'


class StylableObject(RxGUIObject):
    """
    superclass for objects with modifiable size, color, border, etc.
    """
    def __init__(self, name, parent):
        """
        @param name: str name for the REXI object
        @param parent: RxGUIObject parent object
        """
        RxGUIObject.__init__(self, name, parent)
        self._height = ''
        self._width = ''
        self._font = Font.Font(self, "font")
        self._text_color = Color.Color("textColor", "Black")
        self._background_color = Color.Color("backgroundColor", "White")
        self._border = Border.Border(self, "border")
        self._css = ""
        self._style_internal_enabled = False
        self._style_internal = ""

    def set_size(self, width, height):
        """
        set size of the label
        @param width: str width of the label object
        @param height: str height of the label object
        """
        self._height = height
        self._width = width

    def set_font(self, font):
        """
        set the font of the text in the label
        @param font: Font
        """
        self._font = font

    def set_text_color(self, color):
        """
        set the color of the text in the label
        @param color: Color
        """
        self._text_color = color

    def set_background_color(self, color):
        """
        set the background color of the label
        @param color: Color
        """
        self._background_color = color

    def set_border(self, border):
        """
        set border for the label object
        @param border: Border
        """
        self._border = border

    def get_border(self):
        """
        @return: Border label border
        """
        return self._border

    def get_size(self):
        """
        @return : list list of the label's width as str and height as str
        """
        return [self._width, self._height]

    def get_font(self):
        """
        @return : Font the font used for displaying text in the label
        """
        return self._font

    def get_colors(self):
        """
        @return: list list of text color as Color and background color as Color
        """
        return [self._text_color, self._background_color]

    def get_width(self):
        """
        @return: str width of the label
        """
        return self._width

    def get_height(self):
        """
        @return: str height of the label
        """
        return self._height

    def enable_internal_style(self, style):
        """
        enable an internal user-inputted CSS style to the TextEdit object by providing proper CSS
        @param style: str css to be set as internal style
        """
        self._style_internal_enabled = True
        self._style_internal = style

    def disable_internal_style(self):
        """
        disable user-inputted CSS style
        """
        self._style_internal_enabled = False

    def get_style_internal_status(self):
        """
        get a list of a bool and a str, the bool defines whether internal style is enabled and the str is
        the internal style
        @return : list list of style_internal_enabled as boolean and style_internal as str
        """
        return [self._style_internal_enabled, self._style_internal]