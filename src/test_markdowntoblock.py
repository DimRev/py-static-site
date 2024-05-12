import unittest
from mkdn_parse import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_empty_input(self):
        md_text = ""
        expected_result = []
        self.assertEqual(markdown_to_blocks(md_text), expected_result)

    def test_markdown_to_blocks_single_block(self):
        md_text = "This is a single block of text."
        expected_result = ["This is a single block of text."]
        self.assertEqual(markdown_to_blocks(md_text), expected_result)

    def test_markdown_to_blocks_multiple_blocks(self):
        md_text = '''
Block 1: This is the first block of text.
It can span multiple lines and contain newlines.

Block 2: This is the second block of text.
It also has multiple lines and newlines in it.

Block 3: This is the third block of text.
It is separated by empty lines from the previous blocks.

Block 4: This is the fourth block of text.
It follows the same pattern with multiple lines and newlines.
'''
        expected_result = [
            "Block 1: This is the first block of text.\nIt can span multiple lines and contain newlines.",
            "Block 2: This is the second block of text.\nIt also has multiple lines and newlines in it.",
            "Block 3: This is the third block of text.\nIt is separated by empty lines from the previous blocks.",
            "Block 4: This is the fourth block of text.\nIt follows the same pattern with multiple lines and newlines."
        ]
        self.assertEqual(markdown_to_blocks(md_text), expected_result)

if __name__ == '__main__':
    unittest.main()