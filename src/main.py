from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_blocks import block_to_block_type


def main():
    block = "####### this is a heading"
    block_type = block_to_block_type(block)
    print(block_type)


if __name__ == "__main__":
    main()
