import unittest
from gencontent import extract_title


class TestLinksExtract(unittest.TestCase):
    def test_gencontent_normalh1(self):
        markdown = "# Hello World!"
        self.assertEqual(extract_title(markdown), "Hello World!")

    def test_gencontent_trickyh1(self):
        markdown = """![image](/img.png)

# Hello World!"""
        self.assertEqual(extract_title(markdown), "Hello World!")

    def test_gencontent_noh1(self):
        with self.assertRaises(Exception):
            extract_title(">Hello World!")


if __name__ == "__main__":
    unittest.main()
