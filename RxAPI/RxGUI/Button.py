__author__ = 'amentis'
from RxAPI.RxGUI import StylableObject, RxDynamic


class Button(StylableObject, RxDynamic):
    """A button for starting actions on push"""
    def __init__(self, parent, name, value="Button"):
        """
        @param parent: RxGUIObject parent REXI object
        @param name: str name of the REXI object
        @param value: str text label of the button
        """
        StylableObject.__init__(self, name, parent)
        RxDynamic.__init__(self)
        self._parent.add_child(self)
        self._parent.append_javascript("var %s = new Button(\"%s\"); \n" % (self.get_name(), self.get_name()))
        self.__value = value

    def get_value(self):
        """
        @return str text label of the button
        """
        return self.__value

    def set_value(self, value):
        """
        @param value: str text label for the button
        """
        self.__value = value

    def get(self):
        """
        @return: str HTML of the button
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
        <button id="{0}" class="Button" type=\"button\">{1}</button>
            """.format(self.get_name(), self.__value)

javascript_class="""
function Button (name) {
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
    this.get_value = function () {
        $(\"#\" + this.name).html();
    };
    this.set_size = function (width, height) {
        $(\"#\" + this.name).style.width = width;
        $(\"#\" + this.name).style.width = height;
    };
    this.set_value = function (text) {
        $(\"#\" + this.name).text(text).button(\"Refresh\");
    };
}
"""