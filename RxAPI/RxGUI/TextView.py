__author__ = 'amentis'
from RxAPI.RxGUI import StylableObject, RxDynamic, TextContainer


class TextView(StylableObject, RxDynamic, TextContainer):

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
        self._parent.append_javascript("var %s = new TextView(\"%s\"); \n" % (self.get_name(), self.get_name()))

    def get(self):
        """
        @return: str HTML of the text edit field
        """
        style = " "
        if self._style_internal_enabled:
            style += self._style_internal
        style += """
        #%s {color: %s;font: %s;  %s background-color: %s; overflow: auto;}
        """ % (self.get_name(), self._text_color.get(), self._font.get(), self._border.get(),
               self._background_color.get())

        style += self._css
        self._parent.add_css(style)
        self._parent.append_javascript(self.get_javascript())

        return """
        <p id=\"{0}\" class=\"TextView\">{1}</p>
            """ .format(self.get_name(), self._text)


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