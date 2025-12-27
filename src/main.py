from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


def main():
    # node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # print(node)
    fisk = "This is text with a **bolded phrase** in the middle"
    # split_nodes_delimiter()

    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    split_nodes_delimiter([node], "`", TextType.CODE)


main()
