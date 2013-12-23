__author__ = 'amentis'
from RxAPI.RxGUI import Color, RxGUIObject


class Border(RxGUIObject):
    """
    Drawable border for any drawable RxGUIObject.
    """
    def __init__(self, name, color=None, style="solid", width="1px"):
        """
        @param name: str
        @param color: Color
        @param style: str
        none, hidden, dotted, dashed, solid, double, groove, ridge, inset, outset, inherit
        @param width: str
        thin, medium, thick, N%/px/cm/etc., inherit
        """
        RxGUIObject.__init__(self, name, None)
        self._style = style
        self._width = width
        if color is None:
            self._color = Color.Color()
            self._color.color_by_name('Black')
        else:
            self._color = color

    def get(self):
        """
        @rtype : str
        @return : portion of CSS, defining the border
        """
        return "border: %s %s %s ;" % (self._width, self._style, self._color.get())