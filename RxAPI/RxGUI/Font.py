__author__ = 'amentis'
from RxAPI.RxGUI import RxGUIObject


class Font(RxGUIObject):
    """
    text font definition for wherever such is needed
    """

    def __init__(self, parent, name,
                 family="Arial, sans-serif", style="normal", size="medium", variant="normal",
                 weight="normal", line_height="normal"):
        """
        @param parent: RxGUIObject parent object
        @param name: str name of the REXI object
        @param family: str font-family - list of font names, ending with a base name
        acceptable values: list of any fonts + one these bases: serif, sans-serif, monospace
        @param style: str font-style acceptable values: normal, italic, oblique, inherit
        @param size: str font-size acceptable values:
        xx-small, x-small, small, medium, large, x-large, xx-large, smaller, larger,
        N%, Npx/cm,etc., inherit
        @param variant: str font-variant acceptable values: normal, small-caps, inherit
        @param weight: str font-variant acceptable values:
        normal, bold, bolder, lighter, 100, 200, 300 ... 900, inherit
        @param line_height: str acceptable values: normal, number multiplied with current font size,
        Npx,cm,etc., %, inherit
        """
        RxGUIObject.__init__(self, name, parent)
        self._family = family
        self._style = style
        self._size = size
        self._variant = variant
        self._weight = weight
        self._line_height = line_height

    def get(self):
        """
        @return: str CSS code defining the font
        """
        return """%s %s %s %s/%s %s"""%(
            self._style, self._variant, self._weight, self._size, self._line_height, self._family)