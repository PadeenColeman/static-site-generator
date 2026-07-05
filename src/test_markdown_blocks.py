import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType


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


if __name__ == "__main__":
    unittest.main()
