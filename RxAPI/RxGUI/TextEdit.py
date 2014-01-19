__author__ = 'amentis'
from RxAPI.RxGUI import StylableObject, RxDynamic, TextContainer


class TextEdit(StylableObject, RxDynamic, TextContainer):
    """A GUI field for working with user-inputted multi-line text"""

    def __init__(self, parent, name, text=" "):
        """
        @param parent: RxGUIObject parent REXI object
        @param name: str name of the REXI object
        @param text: str value of the text input field
        """
        StylableObject.__init__(self, name, parent)
        RxDynamic.__init__(self)
        TextContainer.__init__(self, text)
        self._parent.add_child(self)
        self._parent.append_javascript("var %s = new TextEdit(\"%s\"); \n" % (self.get_name(), self.get_name()))

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
        <textarea id="{0}" class="TextEdit">{1}</textarea>
            """.format(self.get_name(), self._text)


javascript_class="""
function TextEdit (name) {
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