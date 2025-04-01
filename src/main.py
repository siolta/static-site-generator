from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_blocks import block_to_block_type
from markdown_to_html import markdown_to_html_node


def main():
    md = """
##### HEADING

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    md_code = """
```
This is text that _should_ remain 
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)


if __name__ == "__main__":
    main()
