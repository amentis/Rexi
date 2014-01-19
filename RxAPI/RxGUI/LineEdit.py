__author__ = 'amentis'

from RxAPI.RxGUI import RxDynamic, StylableObject, TextContainer


class LineEdit(StylableObject, RxDynamic, TextContainer):
    """
    text input field of one line
    """

    def __init__(self, parent, name, text=" "):
        """
        @param parent: RxGUIObject parent REXI object
        @param name: str name of the REXI object
        @param text: str value of the line edit field
        """
        StylableObject.__init__(self, name, parent)
        RxDynamic.__init__(self)
        TextContainer.__init__(self, text)
        self._max_length = ' '
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