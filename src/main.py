from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    node = TextNode("this is some text", TextType.IMAGE, "https://test.link")
    print(node)
    html_node = text_node_to_html_node(node)

    print(html_node)


if __name__ == "__main__":
    main()
