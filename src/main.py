from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from node_helpers import split_nodes_delimiter


def main():
    node1 = TextNode("This is text with `code block` words", TextType.TEXT)
    node2 = TextNode("This is second text with `code block` words", TextType.TEXT)
    node3 = TextNode("**code block**", TextType.BOLD)
    new_nodes = split_nodes_delimiter([node1, node2, node3], "`", TextType.CODE)
    print(new_nodes)


if __name__ == "__main__":
    main()
