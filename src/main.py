from textnode import TextNode, TextType


def main():
    text = "This is some text"
    url = "www.bootdev.dev"
    node = TextNode(text, TextType.TEXT, url)
    print(node)


main()
