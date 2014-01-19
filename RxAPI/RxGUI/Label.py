__author__ = 'amentis'

from RxAPI.RxGUI import StylableObject, RxDynamic, TextContainer


class Label(StylableObject, RxDynamic, TextContainer):
    """
    label object containing simple text
    """

    def __init__(self, parent, name, text=None):
        """
        @param parent: RxGUIObject parent object
        @param name: str name of the REXI object
        @param text: str text to be shown in the label
        """
        StylableObject.__init__(self, name, parent)
        RxDynamic.__init__(self)
        if not text:
            text = name
        TextContainer.__init__(self, text)
        self._parent.add_child(self)

    def get(self):
        """
        @return: str  HTML code of the label
        """
        if self._style_internal_enabled:
            self._css += self._style_internal
        self._parent.add_css(self._css)
        self._parent.append_javascript(self.get_javascript())
        return """
        <span id=\"%s\" class=\"label\"> %s </span>
            """ % (self.get_name(), self.get_text())