import unittest
from mkdn_parse import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), "heading 1")
    def test_heading(self):
        block = "## This is a heading"
        self.assertEqual(block_to_block_type(block), "heading 2")
    def test_heading(self):
        block = "### This is a heading"
        self.assertEqual(block_to_block_type(block), "heading 3")
    def test_heading(self):
        block = "#### This is a heading"
        self.assertEqual(block_to_block_type(block), "heading 4")
    def test_heading(self):
        block = "##### This is a heading"
        self.assertEqual(block_to_block_type(block), "heading 5")
    def test_heading(self):
        block = "###### This is a heading"
        self.assertEqual(block_to_block_type(block), "heading 6")

    def test_code_block(self):
        block = "```\nThis is a code block\n```"
        self.assertEqual(block_to_block_type(block), "code")

    def test_unordered_list(self):
        block = '''* Item 1
* Item 2
* Item 3'''
        self.assertEqual(block_to_block_type(block), "unordered list")

    def test_ordered_list(self):
        block = '''1. Item 1
2. Item 2
3. Item 3'''
        self.assertEqual(block_to_block_type(block), "ordered list")

    def test_quote_block(self):
        block = "> This is a quote block"
        self.assertEqual(block_to_block_type(block), "quote block")

    def test_regular_text(self):
        block = "This is regular text"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_empty_block(self):
        block = ""
        with self.assertRaises(ValueError):
            block_to_block_type(block)
            
    def test_mixed_list(self):
        block = '''1. Item 1
* Item 2
3. Item 3'''
        self.assertEqual(block_to_block_type(block), "paragraph")

if __name__ == '__main__':
    unittest.main()
