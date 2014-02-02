__author__ = 'amentis'


class TextContainer:
    """
    superclass for objects containing text
    """
    def __init__(self, text):
        """
        @param text: value of the text object
        """
        self._text = text

    def set_text(self, text):
        """
        set a value for the text object
        @param text: str value of the text object
        """
        self._text = text

    def get_text(self):
        """
        @return : value of the text object
        """
        return self._text

    def append_text(self, text):
        """
        add text to the end of the value of the text object
        @param text: text to be appended
        """
        self._text += text

    def prepend_text(self, text):
        """
        add text to the beginning of the value of the text object
        @param text: text to be appended
        """
        self._text = text + self._text

    def clear_text(self):
        """
        erase the value of the text edit field
        """
        self._text = ""