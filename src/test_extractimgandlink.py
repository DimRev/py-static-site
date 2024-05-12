import unittest

from split import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractions(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is an ![example](https://example.com/image.jpg) of a markdown image."
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0][0], "example")
        self.assertEqual(images[0][1], "https://example.com/image.jpg")

        text_no_image = "This text has no markdown image."
        no_images = extract_markdown_images(text_no_image)
        self.assertEqual(len(no_images), 0)

    def test_extract_markdown_links(self):
        text = "This is a [link](https://example.com) to an example."
        links = extract_markdown_links(text)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0][0], "link")
        self.assertEqual(links[0][1], "https://example.com")

        text_no_link = "This text has no markdown link."
        no_links = extract_markdown_links(text_no_link)
        self.assertEqual(len(no_links), 0)

if __name__ == "__main__":
    unittest.main()
