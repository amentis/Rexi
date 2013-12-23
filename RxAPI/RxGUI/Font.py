__author__ = 'amentis'
from RxAPI.RxGUI import RxGUIObject


class Font(RxGUIObject):
    def __init__(self, parent, name,
                 family="Arial, sans-serif", style="normal", size="medium", variant="normal",
                 weight="normal", line_height="normal"):
        """
        @param parent: RxGUIObject
        @param name: str
        @param family: str
        font-family - list of font names, ending with a base name (serif, sans-serif, monospace)
        @param style: str
        font-style - normal, italic, oblique, inherit
        @param size: str
        font-size -  xx-small, x-small, small, medium, large, x-large, xx-large, smaller, larger,
         N%, Npx/cm,etc., inherit
        @param variant: str
        font-variant - normal, small-caps, inherit
        @param weight: str
        font-variant - normal, bold, bolder, lighter, 100, 200, 300 ... 900, inherit
        @param line_height: str
        normal, number multiplied with current font size, Npx,cm,etc., %, inherit
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

        @rtype : str
        @return: portion of CSS, defining the font
        """
        return """%s %s %s %s/%s %s"""%(
            self._style, self._variant, self._weight, self._size, self._line_height, self._family)