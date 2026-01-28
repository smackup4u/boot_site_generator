class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
            dict = self.props
            html_str = " "
            for item in dict:
                html_str = html_str + item + "=" + f"\"{dict[item]}\"" + " "
            return html_str

        else:
            return None
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        if isinstance(other, HTMLNode) == False:
            return False
        else:
            if self.tag == other.tag and self.value == other.value and self.props == other.props:
                return True
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, children, props)        
