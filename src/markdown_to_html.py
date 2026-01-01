from htmlnode import HTMLNode
from markdown_blocks import block_to_block_type, markdown_to_blocks


def markdown_to_html_node(markdown):
    new_list = []

    blocklist = markdown_to_blocks(markdown)
    for block in blocklist:
        block_type = block_to_block_type(block)
        new_list.append(HTMLNode(block, block_type))
    return new_list
