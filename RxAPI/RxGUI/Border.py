__author__ = 'amentis'
from RxAPI.RxGUI import Color, RxGUIObject


class Border(RxGUIObject):
    """
    Drawable border for any drawable RxGUIObject.
    """
    def __init__(self, name, color=None, style="solid", width="1px"):
        """
        @param name: str name of the REXI object
        @param color: Color color of the border
        @param style: str style of the border, acceptable values:
        none, hidden, dotted, dashed, solid, double, groove, ridge, inset, outset, inherit
        @param width: str width of the border, acceptable values:
        thin, medium, thick, N%/px/cm/etc., inherit
        """
        RxGUIObject.__init__(self, name, None)
        self._style = style
        self._width = width
        if color is None:
            self._color = Color.Color('borderColor')
            self._color.color_by_name('Black')
        else:
            self._color = Color.Color('borderColor', color)

    def get(self):
        """
        @return : str CSS code defining the border
        """
        return "border: %s %s %s ;" % (self._width, self._style, self._color.get())