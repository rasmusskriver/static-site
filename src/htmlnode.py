class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):

        the_string = ""

        if self.props == None:
            return

        for prop in self.props:
            the_key = self.props[prop]
            the_string += f'{prop}="{the_key}" '

        return the_string

    def __repr__(self):
        return f"HTMLNode: tag={self.tag} value={self.value} children={self.children} props={self.props}"
