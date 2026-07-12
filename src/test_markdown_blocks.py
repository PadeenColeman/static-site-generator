import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
    markdown_to_html_node,
)


class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_2(self):
        md = """
**Markdown** is a _lightweight_ markup language.

It supports `inline code` and **bold** or _italic_ text easily.

Key features:

- Simple syntax
- Readable raw text
- Wide support

Use it for _docs_, **notes**, or `README` files — it's versatile and fast to learn.
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "**Markdown** is a _lightweight_ markup language.",
                "It supports `inline code` and **bold** or _italic_ text easily.",
                "Key features:",
                "- Simple syntax\n- Readable raw text\n- Wide support",
                "Use it for _docs_, **notes**, or `README` files — it's versatile and fast to learn.",
            ],
        )

    def test_heading_block(self):
        md = "## Test"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_block_neg(self):
        md = "####### Test"
        block_type = block_to_block_type(md)
        self.assertNotEqual(block_type, BlockType.HEADING)

    def test_code_block(self):
        md = "```\nsome nice code```"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.CODE)

    def test_code_block_neg(self):
        md = "```some still nicer code```"
        block_type = block_to_block_type(md)
        self.assertNotEqual(block_type, BlockType.CODE)

    def test_quote_block(self):
        md = ">And Homer said\n>More energy."
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_quote_block_neg(self):
        md = ">And Homer said\n<More energy you fools."
        block_type = block_to_block_type(md)
        self.assertNotEqual(block_type, BlockType.QUOTE)

    def test_unordered_list_block(self):
        md = "- sleeping bag\n- socks\n- tent\n- knife"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_unordered_list_block_neg(self):
        md = "-milk\n-beer\n-water"
        block_type = block_to_block_type(md)
        self.assertNotEqual(block_type, BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        md = "1. sleeping bag\n2. socks\n3. tent\n4. knife"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_ordered_list_block_neg(self):
        md = "1.milk\n2.beer\n3.water"
        block_type = block_to_block_type(md)
        self.assertNotEqual(block_type, BlockType.ORDERED_LIST)

    def test_ordered_list_block_neg(self):
        md = "1. milk\n3. beer\n4. water"
        block_type = block_to_block_type(md)
        self.assertNotEqual(block_type, BlockType.ORDERED_LIST)

    def test_paragraph_block(self):
        md = "I am just a paragraph."
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_headings2(self):
        md = "## This is a level 2 heading"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>This is a level 2 heading</h2></div>",
        )

    def test_headings5(self):
        md = "##### This is a level 5 heading"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h5>This is a level 5 heading</h5></div>",
        )

    def test_quotes(self):
        md = """
> This is a quote
> over several lines
> about some code
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote over several lines about some code</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- Milk
- Eggs
- Apples
- Beer
- Butter
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Milk</li><li>Eggs</li><li>Apples</li><li>Beer</li><li>Butter</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. Milk
2. Eggs
3. Apples
4. Beer
5. Butter
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Milk</li><li>Eggs</li><li>Apples</li><li>Beer</li><li>Butter</li></ol></div>",
        )


if __name__ == "__main__":
    unittest.main()
