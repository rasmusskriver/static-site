from markdown_blocks import markdown_to_blocks
from markdown_to_html import markdown_to_html_node
from textnode import TextNode, TextType


def main():
    # node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # print(node)

    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    print(markdown_to_html_node(md))


main()
