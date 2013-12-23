__author__ = 'amentis'
from RxAPI.RxGUI import Font, Color, Border, RxGUIObject, RxDynamic


class TextView(RxGUIObject, RxDynamic):

    def __init__(self, parent, name, text=" "):
        """

        @param parent: RxGUIObject
        @param name: str
        @param text: str
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

        @param width: str
        @param height: str
        """
        self.__height = height
        self.__width = width

    def enable_internal_style(self, style):
        """

        @param style: str
        """
        self.__style_internal_enabled = True
        self.__style_internal = style

    def disable_internal_style(self):
        self.__style_internal_enabled = False

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

    def get_style_internal_status(self):
        """

        @rtype : list
        @return : list of internal style enabled as boolean and internal style as str
        """
        return [self.__style_internal_enabled, self.__style_internal]

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

    def get(self):
        """


        @return: HTML of the text view widget
        @rtype: str
        """
        style = " "
        if self.__style_internal_enabled:
            style += self.__style_internal
        style += """
        #%s {color: %s;font: %s;  %s background-color: %s;}
        """ % (self.get_name(), self.__text_color.get(), self.__font.get(), self.__border.get(),
               self.__background_color.get())

        style += self.__css
        self._parent.add_css(style)
        self._parent.append_javascript(self.get_javascript())

        return """
        <p id="{0}">{1}</p>
            """ .format(self.get_name(), self.__text)

    def set_size(self, width, height):
        """

        @param width: str
        @param height: str
        """
        self.__width = width
        self.__height = height

        self.__css += """
            #%s {display: block; width: %s; height: %s; }
            """ % (self.get_name(), self.__width, self.__height)

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

javascript_class = """
function TextView (name) {
    this.name = name;
    this.set_size = function(width, height) {
        document.getElementById(this.name).style.width = width;
        document.getElementById(this.name).style.height = height;
    };
    this.get_font = function() {
        return document.getElementById(this.name).style.font;
    };
    this.get_colors = function() {
        return [document.getElementById(this.name).style.color, document.getElementById(name).background-color];
    };
    this.get_text = function () {
        return document.getElementById(this.name).innerHTML;
    };
    this.set_size = function (width, height) {
        document.getElementById(this.name).style.width = width;
        document.getElementById(this.name).style.width = height;
    };
    this.set_text = function (text) {
        document.getElementById(this.name).innerHTML = text;
    };
}
"""