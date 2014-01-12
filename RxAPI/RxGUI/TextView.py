__author__ = 'amentis'
from RxAPI.RxGUI import Font, Color, Border, RxGUIObject, RxDynamic


class TextView(RxGUIObject, RxDynamic):

    def __init__(self, parent, name, text=" "):
        """
        @param parent: RxGUIObject parent REXI object
        @param name: str name of the REXI object
        @param text: str value of the text input field
        """
        RxGUIObject.__init__(self, name, parent)
        RxDynamic.__init__(self)
        self.__height = ''
        self.__width = ''
        self.__style_internal_enabled = False
        self.__style_internal = ""
        self.__font = Font.Font(self, "font")
        self.__text_color = Color.Color("textColor")
        self.__background_color = Color.Color("backgroundColor")
        self.__text = text
        self.__border = Border.Border(self, "border")
        self._parent.add_child(self)
        self.__css = ""
        self._parent.append_javascript("var %s = new TextView(\"%s\"); \n" % (self.get_name(), self.get_name()))

    def set_size(self, width, height):
        """
        set the size for the TextEdit object
        @param width: str
        @param height: str
        """
        self.__height = height
        self.__width = width

    def enable_internal_style(self, style):
        """
        enable an internal user-inputted CSS style to the TextEdit object by providing proper CSS
        @param style: str css to be set as internal style
        """
        self.__style_internal_enabled = True
        self.__style_internal = style

    def disable_internal_style(self):
        """
        disable user-inputted CSS style
        """
        self.__style_internal_enabled = False

    def set_font(self, font):
        """
        disable user-inputted CSS style
        """
        self.__font = font

    def set_text_color(self, color):
        """
        set the color for the text in the TextEdit object
        @param color: Color
        """
        self.__text_color = color

    def set_background_color(self, color):
        """
        set the background color for the TextEdit object
        @param color: Color
        """
        self.__background_color = color

    def set_border(self, border):
        """
        set a border for the TextEdit object
        @param border: Color
        """
        self.__border = border

    def get_border(self):
        """
        @return: Border border of the text edit widget
        """
        return self.__border

    def set_text(self, text):
        """
        set a value for the TextEdit object
        @param text: str value of the text field
        """
        self.__text = text

    def get_size(self):
        """
        get the size of the TextEdit object
        @return list list of width as str and height as str
        """
        return [self.__width, self.__height]

    def get_style_internal_status(self):
        """
        get a list of a bool and a str, the bool defines whether internal style is enabled and the str is
        the internal style
        @return : list list of style_internal_enabled as boolean and style_internal as str
        """
        return [self.__style_internal_enabled, self.__style_internal]

    def get_font(self):
        """
        @return: Font font of the text in the TextEdit object
        """
        return self.__font

    def get_colors(self):
        """
        @return : list of text color as str and background_color as str
        """
        return [self.__text_color, self.__background_color]

    def get_text(self):
        """
        @return : text of the text edit field
        """
        return self.__text

    def append_text(self, text):
        """
        add text to the end of the value of the text edit field
        @param text: text to be appended
        """
        self.__text += text

    def prepend_text(self, text):
        """
        add text to the beginning of the text edit field
        @param text: text to be appended
        """
        self.__text = text + self.__text

    def clear_text(self):
        """
        erase the value of the text edit field
        """
        self.__text = ""

    def get(self):
        """
        @return: str HTML of the text edit field
        """
        style = " "
        if self.__style_internal_enabled:
            style += self.__style_internal
        style += """
        #%s {color: %s;font: %s;  %s background-color: %s; overflow: auto;}
        """ % (self.get_name(), self.__text_color.get(), self.__font.get(), self.__border.get(),
               self.__background_color.get())

        style += self.__css
        self._parent.add_css(style)
        self._parent.append_javascript(self.get_javascript())

        return """
        <p id=\"{0}\" class=\"TextView\">{1}</p>
            """ .format(self.get_name(), self.__text)

    def get_width(self):
        """
        @return: str width of the text edit field
        """
        return self.__width

    def get_height(self):
        """
        @return: str height of the text edit field
        """
        return self.__height

javascript_class = """
function TextView (name) {
    this.name = name;
    this.set_size = function(width, height) {
        $(\"#\" + this.name).style.width = width;
        $(\"#\" + this.name).style.height = height;
    };
    this.get_font = function() {
        $(\"#\" + this.name).style.font;
    };
    this.get_colors = function() {
        return [$(\"#\" + this.name).style.color, $(\"#\" + this.name).background-color];
    };
    this.get_text = function () {
        return $(\"#\" + this.name).html();
    };
    this.set_size = function (width, height) {
        $(\"#\" + this.name).style.width = width;
        $(\"#\" + this.name).style.width = height;
    };
    this.set_text = function (text) {
        $(\"#\" + this.name).text(text);
    };

    this.append_text = function (text) {
        $(\"#\" + this.name).html($(\"#\" + this.name).html() + text);
    };
    this.prepend_text = function (text) {
        $(\"#\" + this.name).text(text + $(\"#\" + this.name).text());
    };
    this.clear_text = function () {
        $(\"#\" + this.name).text(\"\");
    };
}
"""