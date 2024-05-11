import unittest
from main import text_node_to_html_node 
from textnode import TextNode, TextType 
from leafnode import LeafNode

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_type_text(self):
        text_node = TextNode("Hello", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello")
        self.assertEqual(html_node.props, None)

    def test_text_type_bold(self):
        text_node = TextNode("Bold Text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold Text")
        self.assertEqual(html_node.props, None)

    def test_text_type_italic(self):
        text_node = TextNode("Italic Text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic Text")
        self.assertEqual(html_node.props, None)

    def test_text_type_code(self):
        text_node = TextNode("Code Example", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code Example")
        self.assertEqual(html_node.props, None)

    def test_text_type_link(self):
        text_node = TextNode("Click Here", TextType.LINK, url="https://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click Here")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_text_type_image(self):
        text_node = TextNode("Image", TextType.IMAGE, url="https://example.com/image.jpg")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "https://example.com/image.jpg", "alt": "Image"})

if __name__ == "__main__":
    unittest.main()
