from enum import Enum


class TextType(Enum):
    TEXT = "text"


class TextNode:
    def __init__(self, text):
        self.text = text
        self.text_type = TextType
        self.url = None

    def __eq__(self, other):
        if not TextType(self, other):
            return NotImplemented

    def __repr__(self):
        return f"TextNode(text={self.text}, text_type={self.text_type}, url={self.url})"
