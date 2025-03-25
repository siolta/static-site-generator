import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
