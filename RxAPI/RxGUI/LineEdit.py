__author__ = 'amentis'

from RxAPI.RxGUI import RxDynamic, RxGUIObject, Font, Color, Border


class LineEdit(RxGUIObject, RxDynamic):
    """
    text input field of one line
    """

    def __init__(self, parent, name, text=" "):
        """
        @param parent: RxGUIObject parent REXI object
        @param name: str name of the REXI object
        @param text: str value of the line edit field
        """
        RxGUIObject.__init__(self, name, parent)
        RxDynamic.__init__(self)
        self._height = ''
        self._width = ''
        self._max_length = ''
        self._style_internal_enabled = False
        self._style_internal = ""
        self._css = ""
        self._font = Font(self, "font")
        self._text_color = Color("textColor")
        self._background_color = Color("backgroundColor", "White")
        self._text = text
        self._border = Border(self, "border")
        self._parent.add_child(self)
        self._parent.append_javascript("var %s = new TextEdit(\"%s\"); \n" % (self.get_name(), self.get_name()))

    def set_max_length(self, max_length):
        """
        set maximum length of the text in the field
        @param max_length: int number of symbols
        """
        self._max_length = max_length

    def get_max_length(self):
        """
        @return: int maximum number of symbols that fit in the field
        """
        return self._max_length

    def enable_internal_style(self, style):
        """
        enable an internal user-inputted CSS style to the TextEdit object by providing proper CSS
        @param style: str
        """
        self._style_internal_enabled = True
        self._style_internal = style

    def disable_internal_style(self):
        """
        disable user-inputted CSS style
        """
        self._style_internal_enabled = False

    def set_font(self, font):
        """
        sets the font for the text in the TextEdit object
        @param font: Font
        """
        self._font = font

    def set_text_color(self, color):
        """
        set the color for the text in the TextEdit object
        @param color: Color
        """
        self._text_color = color

    def set_background_color(self, color):
        """
        set the background color for the TextEdit object
        @param color: Color background color
        """
        self._background_color = color

    def set_border(self, border):
        """
        set the border for the TextEdit object
        @param border: Border
        """
        self._border = border

    def get_border(self):
        """
        get the border of the TextEdit object
        @return: Border Border of the text edit widget
        """
        return self._border

    def set_text(self, text):
        """
        set a value for the TextEdit object
        @param text: str new value
        """
        self._text = text

    def get_size(self):
        """
        get the size of the TextEdit object
        @return list list of width as str and height as str
        """
        return [self._width, self._height]

    def get_style_internal_status(self):
        """
        get a list of a bool and a str, the bool defines whether internal style is enabled and the str is
        the internal style
        @return : list list of style_internal_enabled as boolean and style_internal as str
        """
        return [self._style_internal_enabled, self._style_internal]

    def get_font(self):
        """
        get the font of the text in the TextEdit object
        @return: Font
        """
        return self._font

    def get_colors(self):
        """
        get the list of the text color as str and the background color as str
        @return : list list of text color as str and background_color as str
        """
        return [self._text_color, self._background_color]

    def get_text(self):
        """
        @return : str text of the line edit field
        """
        return self._text

    def append_text(self, text):
        """
        add text to the beginning of the text in the field
        @param text: text to be appended
        """
        self._text += text

    def prepend_text(self, text):
        """
        add text after the end of the text in the field
        @param text: text to be prepended
        """
        self._text = text + self._text

    def clear_text(self):
        """
        erase the text in the line edit field
        """
        self._text = ""

    def get(self):
        """
        @return: str HTML of the text edit field
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
        set size for the line edit object
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
        @return: str width of the line edit object
        """
        return self._width

    def get_height(self):
        """
        @return: str height of the line edit object
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