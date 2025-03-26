import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq_text_node(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://test.url")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://test.url")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("First text node", TextType.TEXT)
        node2 = TextNode("Second text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("Text node", TextType.TEXT)
        node2 = TextNode("Text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url_none_type(self):
        node = TextNode("Text node", TextType.CODE, None)
        node2 = TextNode("Text node", TextType.CODE, "https://test.url")
        self.assertNotEqual(node, node2)

    def test_textNode_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://test.url")
        self.assertEqual(
            "TextNode(This is a text node, text, https://test.url)", repr(node)
        )


class TestTextNodeToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_italic(self):
        node = TextNode("This is italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic")

    def test_code(self):
        node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://test.link")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://test.link"})
        self.assertEqual(html_node.value, "This is a link")

    def test_image(self):
        node = TextNode("This is a image node", TextType.IMAGE, "https://test.link")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(
            html_node.props, {"src": "https://test.link", "alt": "This is a image node"}
        )
        self.assertEqual(html_node.value, "")

    def test_error_case(self):
        node = TextNode("", "BADTYPE")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()
