from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


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
    node = ParentNode(
        "p1",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            ParentNode(
                "p2",
                [
                    LeafNode("div2", "div2 text"),
                    LeafNode(None, "Normal2 text"),
                    ParentNode(
                        "p3",
                        [
                            LeafNode("div3", "div3 text"),
                            LeafNode(None, "Normal3 text"),
                        ],
                    ),
                ],
            ),
            LeafNode(None, "Normal text"),
        ],
        {},
    )

    print(node.to_html())


if __name__ == "__main__":
    main()
