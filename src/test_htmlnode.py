import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("h1", "this is a header value", None, {"target": "_blank"})

        self.assertEqual(
            node.__repr__(),
            "HTMLNode(h1, this is a header value, children: None, {'target': '_blank'})",
        )

    def test_child_repr(self):
        child = HTMLNode("p", "this is a paragraph")
        node = HTMLNode("h1", "this is a header value", [child], {"target": "_blank"})

        self.assertEqual(
            repr(node),
            "HTMLNode(h1, this is a header value, children: [HTMLNode(p, this is a paragraph, children: None, None)], {'target': '_blank'})",
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_no_props(self):
        node = HTMLNode("h1", "this is a header value")

        self.assertEqual(node.props_to_html(), "")

    def test_single_prop_to_html(self):
        node = HTMLNode("h1", "this is a header value", props={"target": "_blank"})

        self.assertEqual(node.props_to_html(), ' target="_blank"')

    def test_multiple_prop_to_html(self):
        node = HTMLNode(
            "h1",
            "this is a header value",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
                "text_type": "ITALIC",
            },
        )

        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank" text_type="ITALIC"',
        )


class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode("b", "Text to bold", None)
        self.assertEqual(node.__repr__(), "LeafNode(b, Text to bold, None)")

    def test_no_children(self):
        node = LeafNode("b", "Text to bold", None)
        self.assertEqual(node.children, None)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Here!", {"href": "https://test.link"})
        self.assertEqual(node.to_html(), '<a href="https://test.link">Click Here!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Test Text!")
        self.assertEqual(node.to_html(), "Test Text!")

    def test_leaf_to_html_no_tag_url(self):
        node = LeafNode(None, "Click Here!", {"href": "https://test.link"})
        self.assertEqual(node.to_html(), "Click Here!")

    def test_missing_value_error(self):
        node = LeafNode("a", None)
        with self.assertRaises(ValueError):
            node.to_html()


class TestParentNode(unittest.TestCase):
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_two_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(
            parent_node.to_html(), "<div><span>child</span><span>child2</span></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_mixed_children_empty_subparent(self):
        child_node = LeafNode("b", "grandchild")
        sub_parent_node = ParentNode("span", [])
        parent_node = ParentNode("div", [sub_parent_node, child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span></span><b>grandchild</b></div>",
        )

    def test_to_html_with_mixed_children_and_subparent(self):
        child_node = LeafNode("b", "child1")
        grandchild_node = LeafNode("b", "grandchild")
        sub_parent_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [sub_parent_node, child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span><b>child1</b></div>",
        )


if __name__ == "__main__":
    unittest.main()
