import unittest
from main import split_delimiter
from textnode import TextNode, TextType 
from leafnode import LeafNode

class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter_missing_closing_delimiter(self):
        with self.assertRaises(Exception):
            old_node = TextNode("This `is a test", TextType.TEXT)
            split_delimiter(old_node, "`", TextType.CODE)

    def test_split_delimiter_no_delimiter_found(self):
        old_node = TextNode("Hello World", TextType.TEXT)
        text_nodes = split_delimiter(old_node, "`", TextType.CODE)
        self.assertEqual(len(text_nodes), 1)
        self.assertEqual(text_nodes[0].text, "Hello World")
        self.assertEqual(text_nodes[0].text_type, TextType.TEXT)
        
    def test_split_delimiter_delimiter_block_found(self):
        old_node = TextNode("Hello `code` World", TextType.TEXT)
        text_nodes = split_delimiter(old_node, "`", TextType.CODE)
        self.assertEqual(len(text_nodes), 3)
        self.assertEqual(text_nodes[0].text, "Hello ")
        self.assertEqual(text_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(text_nodes[1].text, "code")
        self.assertEqual(text_nodes[1].text_type, TextType.CODE)
        self.assertEqual(text_nodes[2].text, " World")
        self.assertEqual(text_nodes[2].text_type, TextType.TEXT)
        
    def test_split_delimiter_delimiter_block_found(self):
        old_node = TextNode("Hello *code* World *another*", TextType.TEXT)
        text_nodes = split_delimiter(old_node, "*", TextType.BOLD)
        self.assertEqual(len(text_nodes), 4)
        self.assertEqual(text_nodes[0].text, "Hello ")
        self.assertEqual(text_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(text_nodes[1].text, "code")
        self.assertEqual(text_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(text_nodes[2].text, " World ")
        self.assertEqual(text_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(text_nodes[3].text, "another")
        self.assertEqual(text_nodes[3].text_type, TextType.BOLD)

    def test_split_delimiter_missing_closing_delimiter(self):
        old_node = TextNode("", TextType.TEXT)
        text_nodes = split_delimiter(old_node, "*", TextType.BOLD)
        self.assertEqual(len(text_nodes), 1)
        self.assertEqual(text_nodes[0].text, "")

if __name__ == "__main__":
    unittest.main()