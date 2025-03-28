from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if delimiter in node.text and node.text_type == TextType.TEXT:
            for s in node.text.split(delimiter):
                new_nodes.append(TextNode(s, TextType.TEXT))
            new_nodes[1].text_type = text_type
        else:
            new_nodes.append(node)
    return new_nodes
