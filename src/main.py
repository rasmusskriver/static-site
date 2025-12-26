from textnode import TextNode


def main():
    text = "This is some text"
    text_type = "text"
    url = "www.bootdev.dev"
    node = TextNode(text, text_type, url)
    print(node)


main()
