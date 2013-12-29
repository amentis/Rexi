__author__ = 'amentis'

from RxAPI.RxGUI import LineEdit


class PasswordEdit(LineEdit):
    """
        @param parent: RxGUIObject
        @param name: str
        @param text: str
        """
    def __init__(self, parent, name, text=" "):
        LineEdit.__init__(self, parent, name, text)

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
                    <input type=\"password\" id="{0}" class="LineEdit" value=\"{1}\" />
                        """.format(self.get_name(), self._text)

javascript_class = """
    function PasswordEdit (name) {
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