import re
from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type
from inline_markdown import text_to_textnodes


def heading_count(block):
    match = re.match(r"^#{1,6}", block)
    return len(match.group(0))


def text_to_children(text):
    nodes = []
    for node in text_to_textnodes(text):
        print(text_node_to_html_node(node))
        text_node = text_node_to_html_node(node)
        print(f"text_node: {text_node}")
        nodes.append(text_node)
    return nodes


def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    nodes = []
    for block in blocks:
        children = text_to_children(block)

        match block_to_block_type(block):
            # case BlockType.HEADING:
            #     node = LeafNode(f"<h{heading_count(block)}>", block)
            #     nodes.append(node)
            case BlockType.QUOTE:
                pass
            case BlockType.ULIST:
                pass
            case BlockType.OLIST:
                pass
            case BlockType.PARAGRAPH:
                node = ParentNode("p", children)
                nodes.append(node)
            case BlockType.CODE:
                _text = TextNode(block, "code")
                node = text_node_to_html_node(_text)
                nodes.append(node)

    html_node = ParentNode("div", nodes)
    return html_node
