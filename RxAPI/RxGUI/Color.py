__author__ = 'amentis'
from RxAPI.RxGUI import RxGUIObject


class Color(RxGUIObject):
    """
    color definition for wherever such is needed
    """
    def __init__(self, name, color="Black"):
        """
        @param name: str name of the REXI object
        @param color: str color name. Acceptable values - HTML colors or the following predefined color names:
        AliceBlue, AntiqueWhile, Aqua, Aquamarine, Azure, Beige, Bisque, Black, BlanchedAlmond, Blue,
        BlueViolet, Brown, BurlyWood, Chartreuse, Chocolate, Coral, CornflowerBlue, Cornsilk, Crimson,
        Cyan, DarkBlue, DarkCyan, DarkGoldenRod, DarkGray, DarkGreen, DarkKhaki, DarkMagenta, DarkOliveGreen,
        DarkOrange, DarkOrchid, DarkRed, DarkSalmon, DarkSeaGreen, DarkSlateBlue, DarkSlateGray, DarkTurquoise,
        DarkViolet, DeepPink, DeepSkyBlue, DimGray, DodgerBlue, FireBrick, FloralWhite, ForestGreen, Fuchsia,
        Gainsboro, GhostWhite, Gold, GoldenRod, Gray, Green, GreenYellow, HoneyDew, HotPink, IndianRed, Indigo,
        Ivory, Khaki, Lavender, LavenderBlush, LawnGreen, LemonChiffon, LightBlue, LightCoral, LightCyan,
        LightGoldenRodYellow, LightGray, LightGreen, LightPink, LightSalmon, LightSeaGreen, LightSkyBlue,
        LightSlateGray, LightSteelBlue, LightYellow, Lime, LimeGreen, Linen, Magenta, Maroon, MediumAquaMarine,
        MediumBlue, MediumOrchid, MediumPurple, MediumSeaGreen, MediumSlateBlue, MediumSpringGreen,
        MediumTurquoise, MediumVioletRed, MidnightBlue, MintCream, MistyRose, Moccasin, NavajoWhite, Navy,
        OldLace, Olive, OliveDrab, Orange, OrangeRed, Orchid, PaleGoldenRod, PaleGreen, PaleTurquoise,
        PaleVioletRed, PapayaWhip, PeachPuff, Peru, Pink, Plum, PowderBlue, Purple, Red, RosyBrown, RoyalBlue,
        SaddleBrown, Salmon, SandyBrown, SeaGreen, SeaShell, Sienna, Silver, SkyBlue, SlateBlue, SlateGray,
        Snow, SpringGreen, SteelBlue, Tan, Teal, Thistle, Tomato, Turquoise, Violet, Wheat, White, WhiteSmoke,
        Yellow, YellowGreen
        """
        RxGUIObject.__init__(self, name, None)
        self.__color_names = dict()
        self.__color_names['AliceBlue'] = "#F0F8FF"
        self.__color_names['AntiqueWhite'] = "#FAEBD7"
        self.__color_names['Aqua'] = "#00FFFF"
        self.__color_names['Aquamarine'] = "#7FFFD4"
        self.__color_names['Azure'] = "#F0FFFF"
        self.__color_names['Beige'] = "#F5F5DC"
        self.__color_names['Bisque'] ="#FFE4C4"
        self.__color_names['Black'] = "#000000"
        self.__color_names['BlanchedAlmond'] = "#FFEBCD"
        self.__color_names['Blue'] = "#0000FF"
        self.__color_names['BlueViolet'] = "#8A2BE2"
        self.__color_names['Brown'] = "#A52A2A"
        self.__color_names['BurlyWood'] = "#DEB887"
        self.__color_names['Chartreuse'] = "#7FFF00"
        self.__color_names['Chocolate'] = "##D2691E"
        self.__color_names['Coral'] = "#FF7F50"
        self.__color_names['CornflowerBlue'] = "#6495ED"
        self.__color_names['Cornsilk'] = "#FFF8DC"
        self.__color_names['Crimson'] = "#DC143C"
        self.__color_names['Cyan'] = "#00FFFF"
        self.__color_names['DarkBlue'] = "#00008B"
        self.__color_names['DarkCyan'] = "#008B8B"
        self.__color_names['DarkGoldenRod'] = "#B8860B"
        self.__color_names['DarkGray'] = "#A9A9A9"
        self.__color_names['DarkGreen'] = "#006400"
        self.__color_names['DarkKhaki'] = "#BDB76B"
        self.__color_names['DarkMagenta'] = "#8B008B"
        self.__color_names['DarkOliveGreen'] = "#556B2F"
        self.__color_names['DarkOrange'] = "#FF8C00"
        self.__color_names['DarkOrchid'] = "#9932CC"
        self.__color_names['DarkRed'] = "#8B0000"
        self.__color_names['DarkSalmon'] = "#E9967A"
        self.__color_names['DarkSeaGreen'] = "#8FBC8F"
        self.__color_names['DarkSlateBlue'] = "#483D8B"
        self.__color_names['DarkSlateGray'] = "#2F4F4F"
        self.__color_names['DarkTurquoise'] = "#00CED1"
        self.__color_names['DarkViolet'] = "#9400D3"
        self.__color_names['DeepPink'] = "#FF1493"
        self.__color_names['DeepSkyBlue'] = "#00BFFF"
        self.__color_names['DimGray'] = "#696969"
        self.__color_names['DodgerBlue'] = "#1E90FF"
        self.__color_names['FireBrick'] = "#B22222"
        self.__color_names['FloralWhite'] = "#FFFAF0"
        self.__color_names['ForestGreen'] = "#228B22"
        self.__color_names['Fuchsia'] = "#FF00FF"
        self.__color_names['Gainsboro'] = "#DCDCDC"
        self.__color_names['GhostWhite'] = "#F8F8FF"
        self.__color_names['Gold'] = "##FFD700"
        self.__color_names['GoldenRod'] = "#DAA520"
        self.__color_names['Gray'] = "#808080"
        self.__color_names['Green'] = "#008000"
        self.__color_names['GreenYellow'] = "#ADFF2F"
        self.__color_names['HoneyDew'] = "#F0FFF0"
        self.__color_names['HotPink'] = "#FF69B4"
        self.__color_names['IndianRed'] = "#CD5C5C"
        self.__color_names['Indigo'] = "#4B0082"
        self.__color_names['Ivory'] = "#FFFFF0"
        self.__color_names['Khaki'] = "#F0E68C"
        self.__color_names['Lavender'] = "#E6E6FA"
        self.__color_names['LavenderBlush'] = "#FFF0F5"
        self.__color_names['LawnGreen'] = "#7CFC00"
        self.__color_names['LemonChiffon'] = "#FFFACD"
        self.__color_names['LightBlue'] = "#ADD8E6"
        self.__color_names['LightCoral'] = "#F08080"
        self.__color_names['LightCyan'] = "#E0FFFF"
        self.__color_names['LightGoldenRodYellow'] = "#FAFAD2"
        self.__color_names['LightGray'] = "#D3D3D3"
        self.__color_names['LightGreen'] = "#90EE90"
        self.__color_names['LightPink'] = "#FFB6C1"
        self.__color_names['LightSalmon'] = "#FFA07A"
        self.__color_names['LightSeaGreen'] = "#20B2AA"
        self.__color_names['LightSkyBlue'] = "#87CEFA"
        self.__color_names['LightSlateGray'] = "#778899"
        self.__color_names['LightSteelBlue'] = "#B0C4DE"
        self.__color_names['LightYellow'] = "#FFFFE0"
        self.__color_names['Lime'] = "#00FF00"
        self.__color_names['LimeGreen'] = "#32CD32"
        self.__color_names['Linen'] = "#FAF0E6"
        self.__color_names['Magenta'] = "#FF00FF"
        self.__color_names['Maroon'] = "#800000"
        self.__color_names['MediumAquaMarine'] = "#66CDAA"
        self.__color_names['MediumBlue'] = "#0000CD"
        self.__color_names['MediumOrchid'] = "#BA55D3"
        self.__color_names['MediumPurple'] = "#9370DB"
        self.__color_names['MediumSeaGreen'] = "#3CB371"
        self.__color_names['MediumSlateBlue'] = "#7B68EE"
        self.__color_names['MediumSpringGreen'] = "#00FA9A"
        self.__color_names['MediumTurquoise'] = "#48D1CC"
        self.__color_names['MediumVioletRed'] = "#C71585"
        self.__color_names['MidnightBlue'] = "#191970"
        self.__color_names['MintCream'] = "#F5FFFA"
        self.__color_names['MistyRose'] = "#FFE4E1"
        self.__color_names['Moccasin'] = "#FFE4B5"
        self.__color_names['NavajoWhite'] = "#FFDEAD"
        self.__color_names['Navy'] = "#000080"
        self.__color_names['OldLace'] = "#FDF5E6"
        self.__color_names['Olive'] = "#808000"
        self.__color_names['OliveDrab'] = "#6B8E23"
        self.__color_names['Orange'] = "#FFA500"
        self.__color_names['OrangeRed'] = "#FF4500"
        self.__color_names['Orchid'] = "#DA70D6"
        self.__color_names['PaleGoldenRod'] = "#EEE8AA"
        self.__color_names['PaleGreen'] = "#98FB98"
        self.__color_names['PaleTurquoise'] = "#AFEEEE"
        self.__color_names['PaleVioletRed'] = "#DB7093"
        self.__color_names['PapayaWhip'] = "#FFEFD5"
        self.__color_names['PeachPuff'] = "#FFDAB9"
        self.__color_names['Peru'] = "#CD853F"
        self.__color_names['Pink'] = "#FFC0CB"
        self.__color_names['Plum'] = "#DDA0DD"
        self.__color_names['PowderBlue'] = "#B0E0E6"
        self.__color_names['Purple'] = "#800080"
        self.__color_names['Red'] = "#FF0000"
        self.__color_names['RosyBrown'] = "#BC8F8F"
        self.__color_names['RoyalBlue'] = "#4169E1"
        self.__color_names['SaddleBrown'] = "#8B4513"
        self.__color_names['Salmon'] = "#FA8072"
        self.__color_names['SandyBrown'] = "#F4A460"
        self.__color_names['SeaGreen'] = "#2E8B57"
        self.__color_names['SeaShell'] = "#FFF5EE"
        self.__color_names['Sienna'] = "#A0522D"
        self.__color_names['Silver'] = "#C0C0C0"
        self.__color_names['SkyBlue'] = "#87CEEB"
        self.__color_names['SlateBlue'] = "#6A5ACD"
        self.__color_names['SlateGray'] = "#708090"
        self.__color_names['Snow'] = "#FFFAFA"
        self.__color_names['SpringGreen'] = "#00FF7F"
        self.__color_names['SteelBlue'] = "#4682B4"
        self.__color_names['Tan'] = "#D2B48C"
        self.__color_names['Teal'] = "#008080"
        self.__color_names['Thistle'] = "#D8BFD8"
        self.__color_names['Tomato'] = "#FF6347"
        self.__color_names['Turquoise'] = "#40E0D0"
        self.__color_names['Violet'] = "#EE82EE"
        self.__color_names['Wheat'] = "#F5DEB3"
        self.__color_names['White'] = "#FFFFFF"
        self.__color_names['WhiteSmoke'] = "#F5F5F5"
        self.__color_names['Yellow'] = "#FFFF00"
        self.__color_names['YellowGreen'] = "#9ACD32"
        if color in self.__color_names:
            self._result = self.__color_names[color]
        else:
            self._result = color

    def color_by_name(self, name):
        """
        sets the Color color to an HTML color by using an HTML name
        @param name: str color name. Acceptable values: HTML colors of the following color names:
            Values: AliceBlue, AntiqueWhite, Aqua, Aquamarine, Azure, Beige, Bisque, Black,
            BlanchedAlmond, Blue, BlueViolet, Brown, BurlyWood, CadetBlue, Chartreuse, Chocolate,
            Coral, CornflowerBlue, Cornsilk, Crimson, Cyan, DarkBlue, DarkCyan, DarkGoldenRod,
            DarkGray, DarkGreen, DarkKhaki, DarkMagenta, DarkOliveGreen, DarkOrange, DarkOrchid,
            DarkRed, DarkSalmon, DarkSeaGreen, DarkSlateBlue, DarkSlateGray, DarkTurquoise,
            DarkViolet, DeepPink, DeepSkyBlue, DimGray, DodgerBlue, FireBrick, FloralWhite,
            ForestGreen, Fuchsia, Gainsboro, GhostWhite, Gold, GoldenRod, Gray, Green,
            GreenYellow, HoneyDew, HotPink, IndianRed, Indigo, Ivory, Khaki, Lavender, LavenderBlush,
            LawnGreen, LemonChiffon, LightBlue, LightCoral, LightCyan, LightGoldenRodYellow,
            LightGray, LightGreen, LightPink, LightSalmon, LightSeaGreen, LightSkyBlue,
            LightSlateGray, LightSteelBlue, LightYellow, Lime, LimeGreen, Linen,Magenta, Maroon,
            MediumAquaMarine, MediumBlue, MediumOrchid, MediumPurple, MediumSeaGreen, MediumSlateBlue,
            MediumSpringGreen, MediumTurquoise, MediumVioletRed, MidnightBlue, MintCream, MistyRose,
            Moccasin, NavajoWhite, Navy, OldLace, Olive, OliveDrab, Orange, OrangeRed, Orchid,
            PaleGoldenRod, PaleGreen, PaleTurquoise, PaleVioletRed, PapayaWhip, PeachPuff, Peru, Pink,
            Plum, PowderBlue, Purple, Red, RosyBrown, RoyalBlue, SaddleBrown, Salmon, SandyBrown,
            SeaGreen, SeaShell, Sienna, Silver, SkyBlue, SlateBlue, SlateGray, Snow, SpringGreen,
            SteelBlue, Tan, Teal, Thistle, Tomato, Turquoise, Violet, Wheat, White, WhiteSmoke,
            Yellow, YellowGreen
        """
        self._result = self.__color_names[name]

    def color_by_rgb(self, r, g, b):
        """
        sets the Color color by provided Red Green and Blue values
        @param r: int Red
        @param g: int Green
        @param b: int Blue
        """
        self._result = "rgb({0:d}, {1:d}, {2:d}".format(r, g, b)

    def color_by_rgba(self, r, g, b, a):
        """
        sets the Color color by provided Red Green Blue and Alpha values
        @param r: int Red
        @param g: int Green
        @param b: int Blue
        @param a: float alpha
        """
        self._result = "rgba({0:d}, {1:d}, {2:d}, {3:1.1f})".format(r, g, b, a)

    def get(self):
        """
        @return: str CSS code defining the color
        """
        return self._result