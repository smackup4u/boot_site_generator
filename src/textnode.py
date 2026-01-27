from enum import Enum

class TextType(Enum):
    PLAIN = "simple text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "coding"
    LINK = "links (anchor)"
    IMAGE = "Images"
"""
plain
**Bold text**
_Italic text_
`Code text`
Links, in this format: [anchor text](url)
Images, in this format: ![alt text](url)


"""

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if isinstance(other, TextNode) == False:
            return False
        else:
            if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
                return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

        