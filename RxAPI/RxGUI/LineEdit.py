__author__ = 'amentis'

from RxAPI.RxGUI import RxDynamic, RxGUIObject, Font, Color, Border


class LineEdit(RxGUIObject, RxDynamic):
    def __init__(self, parent, name, text=" "):
        """
        @param parent: RxGUIObject
        @param name: str
        @param text: str
        """
        RxGUIObject.__init__(self, name, parent)
        RxDynamic.__init__(self)
        self._height = ''
        self._width = ''
        self._max_length = ''
        self._style_internal_enabled = False
        self._style_internal = ""
        self._css = ""
        self._font = Font.Font(self, "font")
        self._text_color = Color.Color("textColor")
        self._background_color = Color.Color("backgroundColor", "White")
        self._text = text
        self._border = Border.Border(self, "border")
        self._parent.add_child(self)
        self._parent.append_javascript("var %s = new TextEdit(\"%s\"); \n" % (self.get_name(), self.get_name()))

    def set_max_length(self, max_length):
        """
        @param max_length: str
        """
        self._max_length = max_length

    def get_max_length(self):
        """
        @return: str
        """
        return self._max_length

    def enable_internal_style(self, style):
        """
        Enables an internal user-inputted CSS style to the TextEdit object by providing proper CSS
        @param style: str
        """
        self._style_internal_enabled = True
        self._style_internal = style

    def disable_internal_style(self):
        """
        Disables user-inputted CSS style
        """
        self._style_internal_enabled = False

    def set_font(self, font):
        """
        Sets the font for the text in the TextEdit object
        @param font: Font
        """
        self._font = font

    def set_text_color(self, color):
        """
        Sets the color for the text in the TextEdit object
        @param color: Color
        """
        self._text_color = color

    def set_background_color(self, color):
        """
        Sets the background color for the TextEdit object
        @param color: Color
        """
        self._background_color = color

    def set_border(self, border):
        """
        Sets a border for the TextEdit object
        @param border: Color
        """
        self._border = border

    def get_border(self):
        """
        Gets the border of the TextEdit object
        @rtype : Border
        @return: Border of the text edit widget
        """
        return self._border

    def set_text(self, text):
        """
        Sets a value for the TextEdit object
        @param text: str
        """
        self._text = text

    def get_size(self):
        """
        Gets the size of the TextEdit object
        @rtype: list
        @return list of width as str and height as str
        """
        return [self._width, self._height]

    def get_style_internal_status(self):
        """
        Gets a list of a bool and a str, the bool defines whether internal style is enabled and the str is the internal
        style
        @rtype : list
        @return : list of style_internal_enabled as boolean and style_internal as str
        """
        return [self._style_internal_enabled, self._style_internal]

    def get_font(self):
        """
        Gets the font of the text in the TextEdit object
        @return: Font
        """
        return self._font

    def get_colors(self):
        """
        Gets the list of the text color as str and the background color as str
        @rtype : list
        @return : list of text color as str and background_color as str
        """
        return [self._text_color, self._background_color]

    def get_text(self):
        """
        gets the text of the
        @rtype : str
        @return : text of the text edit field
        """
        return self._text

    def append_text(self, text):
        self._text += text

    def prepend_text(self, text):
        self._text = text + self._text

    def clear_text(self):
        self._text = ""

    def get(self):
        """

        @rtype : str
        @return: HTML of the text edit field
        """
        style = " "
        if self._style_internal_enabled:
            style += self._style_internal
        style += """
            #%s {color: %s;font: %s;  %s background-color: %s; }
            """ % (self.get_name(), self._text_color.get(), self._font.get(), self._border.get(),
                   self._background_color.get())

        style += self._css

        self._parent.add_css(style)
        self._parent.append_javascript(self.get_javascript())

        return """
            <input type=\"text\" id="{0}" class="LineEdit" value=\"{1}\" />
                """.format(self.get_name(), self._text)

    def set_size(self, width, height):
        """
        @param width: str
        @param height: str
        """
        self._width = width
        self._height = height

        self._css += """
                #%s {display: block; width: %s; height: %s; resize:none; }
                """ % (self.get_name(), self._width, self._height)

    def get_width(self):
        """
        @return: str
        """
        return self._width

    def get_height(self):
        """
        @return: str
        """
        return self._height


javascript_class = """
    function LineEdit (name) {
        this.name = name;
        this.set_size = function(width, height) {
            $(\"#\" + this.name).style.width = width;
            $(\"#\" + this.name).style.height = height;
        };
        this.get_font = function() {
            return $(\"#\" + this.name).style.font;
        };
        this.get_colors = function() {
            return [$(\"#\" + this.name).style.color, $(\"#\" + this.name).background-color];
        };
        this.get_text = function () {
            $(\"#\" + this.name).html();
        };
        this.set_size = function (width, height) {
            $(\"#\" + this.name).style.width = width;
            $(\"#\" + this.name).style.width = height;
        };
        this.get_text = function () {
            return $(\"#\" + this.name).val();
        };
        this.set_text = function (text) {
            $(\"#\" + this.name).val(text);
        };
        this.append_text = function (text) {
            $(\"#\" + this.name).val($(\"#\" + this.name).val() + text);
        };
        this.prepend_text = function (text) {
            $(\"#\" + this.name).val(text + $(\"#\" + this.name).val());
        };
        this.clear_text = function () {
            $(\"#\" + this.name).val(\"\");
        };
    }
    """