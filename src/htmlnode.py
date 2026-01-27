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
    
