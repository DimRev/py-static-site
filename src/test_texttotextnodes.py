import unittest
from textnode import TextNode, TextType
from main import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes_simple(self):
        md_text = "This is **bolded** text."
        expected_result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bolded", TextType.BOLD),
            TextNode(" text.", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(md_text), expected_result)

    def test_text_to_textnodes_with_links(self):
        md_text = "Check out this [link](https://example.com)."
        expected_result = [
            TextNode("Check out this ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(md_text), expected_result)

    def test_text_to_textnodes_with_images(self):
        md_text = "Here is an ![image](https://example.com/image.png)."
        expected_result = [
            TextNode("Here is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(md_text), expected_result)

    def test_text_to_textnodes_complex(self):
        md_text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        expected_result = [
          TextNode("This is ", TextType.TEXT),
          TextNode("text", TextType.BOLD),
          TextNode(" with an ", TextType.TEXT),
          TextNode("italic", TextType.ITALIC),
          TextNode(" word and a ", TextType.TEXT),
          TextNode("code block", TextType.CODE),
          TextNode(" and an ", TextType.TEXT),
          TextNode("image", TextType.IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
          TextNode(" and a ", TextType.TEXT),
          TextNode("link", TextType.LINK, "https://boot.dev")
        ]
        
        self.assertEqual(text_to_textnodes(md_text), expected_result)

if __name__ == '__main__':
    unittest.main()
