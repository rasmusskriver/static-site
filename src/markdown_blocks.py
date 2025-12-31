from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown_block):
    pass


def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    new_list = []
    for line in lines:
        if line == "":
            continue
        new_list.append(line.strip())
    return new_list
