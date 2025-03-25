from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode


def main():
    text_node = TextNode("some test text", TextType.LINK, "https://test.link")
    print(text_node)
    html_child_node = HTMLNode("p", "this is a paragraph")
    html_node = HTMLNode(
        "h1", "this is a header value", [html_child_node], {"target": "_blank"}
    )
    leaf_node = LeafNode("p", "this is a paragraph value", {"target": "leaf_node"})
    print(html_node)
    print(html_node.props_to_html())
    print(leaf_node)
    print(leaf_node.to_html())
    leaf_node_link = LeafNode("a", "Click here!", {"href": "https://test.link"})
    print(leaf_node_link.to_html())
    leaf_node_div = LeafNode("div", "this is a div value")
    print(leaf_node_div.to_html())
    leaf_node_none = LeafNode(None, "this is a div value")
    print(leaf_node_none.to_html())


if __name__ == "__main__":
    main()
