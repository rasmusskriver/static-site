from textnode import TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
            continue

    return new_list
