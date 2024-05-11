import unittest
from main import split_delimiter, split_nodes_links, split_nodes_image
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

    def test_split_delimiter_empty_node(self):
        old_node = TextNode("", TextType.TEXT)
        text_nodes = split_delimiter(old_node, "*", TextType.BOLD)
        self.assertEqual(len(text_nodes), 1)
        self.assertEqual(text_nodes[0].text, "")

    def test_split_images_no_image(self):
        old_node = TextNode("This is a text node without a link", TextType.TEXT)
        text_nodes = split_nodes_image(old_node)
        self.assertEqual(len(text_nodes), 1)
        self.assertEqual(text_nodes[0], old_node)

    def test_split_image_with_image(self):
        old_node = TextNode("This is a text node with an ![image](https://example.com/image.png) image", TextType.TEXT)
        text_nodes = split_nodes_image(old_node)
        self.assertEqual(len(text_nodes), 3)
        self.assertEqual(text_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(text_nodes[0].text, "This is a text node with an ")
        self.assertEqual(text_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(text_nodes[1].url, "https://example.com/image.png")
        self.assertEqual(text_nodes[1].text, "image")
        self.assertEqual(text_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(text_nodes[2].text, " image")

    def test_split_images_with_multiple_images(self):
        old_node = TextNode("This is a text node with multiple images ![image1](https://example.com/image1.png) and ![image2](https://example.com/image2.png)", TextType.TEXT)
        text_nodes = split_nodes_image(old_node)
        self.assertEqual(len(text_nodes), 4)
        self.assertEqual(text_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(text_nodes[0].text, "This is a text node with multiple images ")
        self.assertEqual(text_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(text_nodes[1].url, "https://example.com/image1.png")
        self.assertEqual(text_nodes[1].text, "image1")
        self.assertEqual(text_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(text_nodes[2].text, " and ")
        self.assertEqual(text_nodes[3].text_type, TextType.IMAGE)
        self.assertEqual(text_nodes[3].url, "https://example.com/image2.png")
        self.assertEqual(text_nodes[3].text, "image2")
        
    def test_split_links_no_link(self):
        old_node = TextNode("This is a text node without a link", TextType.TEXT)
        text_nodes = split_nodes_links(old_node)
        self.assertEqual(len(text_nodes), 1)
        self.assertEqual(text_nodes[0], old_node)

    def test_split_link_with_link(self):
        old_node = TextNode("This is a text node with an [link](https://example.com) link", TextType.TEXT)
        text_nodes = split_nodes_links(old_node)
        self.assertEqual(len(text_nodes), 3)
        self.assertEqual(text_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(text_nodes[0].text, "This is a text node with an ")
        self.assertEqual(text_nodes[1].text_type, TextType.LINK)
        self.assertEqual(text_nodes[1].url, "https://example.com")
        self.assertEqual(text_nodes[1].text, "link")
        self.assertEqual(text_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(text_nodes[2].text, " link")

    def test_split_links_with_multiple_links(self):
        old_node = TextNode("This is a text node with multiple links [link1](https://example.com/1) and [link2](https://example.com/2)", TextType.TEXT)
        text_nodes = split_nodes_links(old_node)
        self.assertEqual(len(text_nodes), 4)
        self.assertEqual(text_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(text_nodes[0].text, "This is a text node with multiple links ")
        self.assertEqual(text_nodes[1].text_type, TextType.LINK)
        self.assertEqual(text_nodes[1].url, "https://example.com/1")
        self.assertEqual(text_nodes[1].text, "link1")
        self.assertEqual(text_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(text_nodes[2].text, " and ")
        self.assertEqual(text_nodes[3].text_type, TextType.LINK)
        self.assertEqual(text_nodes[3].url, "https://example.com/2")
        self.assertEqual(text_nodes[3].text, "link2")
        
if __name__ == "__main__":
    unittest.main()