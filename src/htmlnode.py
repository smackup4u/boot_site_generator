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
            html_str = html_str[:-1] #remove the last space when all items are processed
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
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    

    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return self.value
        else:
            if self.props == None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return super().__repr__()
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag is missing")
        elif self.children == None:
            raise ValueError("Children is missing")
        else:
            children_concen = ""
            for item in self.children:
                children_concen = children_concen + item.to_html()
            if self.props == None:
                return f"<{self.tag}>{children_concen}</{self.tag}>"
            else:
                return f"<{self.tag}{self.props_to_html()}>{children_concen}</{self.tag}>"
            


