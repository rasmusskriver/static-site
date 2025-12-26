import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_html_node(self):
        node = HTMLNode(
            "h1",
            "the text inside a paragraph",
            ["h1, p"],
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(
            "HTMLNode: tag=h1 value=the text inside a paragraph children=['h1, p'] props={'href': 'https://www.google.com', 'target': '_blank'}",
            repr(node),
        )
