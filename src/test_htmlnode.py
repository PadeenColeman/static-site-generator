import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"target": "_blank", "href": "https://www.google.com"})
        node2 = " target=_blank href=https://www.google.com"
        self.assertEqual(node.props_to_html(), node2)

    def test_None(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_repr(self):
        node = HTMLNode()
        node2 = "HTMLNode(None, None, None, None)"
        node3 = HTMLNode(props={"target": "_blank"})
        node4 = "HTMLNode(None, None, None, {'target': '_blank'})"
        self.assertEqual(node.__repr__(), node2)
        self.assertEqual(node3.__repr__(), node4)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "world")
        self.assertEqual(node.to_html(), "<b>world</b>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), "<a href=https://www.google.com>Hello, world!</a>"
        )


if __name__ == "__main__":
    unittest.main()
