class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        the_string = ""
        for prop in self.props:
            the_key = self.props[prop]
            the_string += f' {prop}="{the_key}"'
        return the_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value.")

        if self.tag is None:
            return self.value

        props_html = ""
        if self.props:
            for key, val in self.props.items():
                props_html += f' {key}="{val}"'

        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
