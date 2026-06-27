import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter


class TestHTMLNode(unittest.TestCase):
    def test_italic(self):
        node = TextNode("She said *quietly* to him", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("She said ", TextType.TEXT),
                TextNode("quietly", TextType.ITALIC),
                TextNode(" to him", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_bold(self):
        node = TextNode("She said **quietly** to him", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("She said ", TextType.TEXT),
                TextNode("quietly", TextType.BOLD),
                TextNode(" to him", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_code(self):
        node = TextNode("She said `quietly` to him", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("She said ", TextType.TEXT),
                TextNode("quietly", TextType.CODE),
                TextNode(" to him", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
