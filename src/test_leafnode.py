import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
  def __init__(self, methodName: str = "runTest") -> None:
    super().__init__(methodName)
    self.node1 = LeafNode("a", "hello world", {"href":"https://google.com","target":"_blank"})
    self.node2 = LeafNode("a", "hello world", {"href":"https://google.com","target":"_blank"})
    self.node1_repr = "LeafNode(a,hello world,{'href': 'https://google.com', 'target': '_blank'})" 

    self.node3 = LeafNode("a", "Hello world", {"href":"https://google.com","target":"_blank"})
    self.node3_expected = "<a href=\"https://google.com\" target=\"_blank\">Hello world</a>"

    self.node4 = LeafNode(None, "Hello world", None)
    self.node4_expected = "Hello world"

    self.node5 = LeafNode("a", None, None)

    self.node6 = LeafNode("img", None, {"src":"http://example.com", "alt":"Test"})
    self.node6_to_html_expected = "<img src=\"http://example.com\" alt=\"Test\"/>"

    self.node7 = LeafNode("img", "bad value", {"src":"http://example.com", "alt":"Test"})
    
  def test_fully_def_eq(self):
    self.assertEqual(self.node1, self.node2)

  def test_to_html_method(self):
    self.assertEqual(self.node3.to_html(),self.node3_expected)

  def test_to_html_no_tag(self):
    self.assertEqual(self.node4.to_html(),self.node4_expected)

  def test_to_html_image_tag(self):
    self.assertEqual(self.node6.to_html(), self.node6_to_html_expected)

  def test_to_html_img_with_value_val_err(self):
    with self.assertRaises(ValueError):
      self.node7.to_html()    

  def test_to_html_no_value_val_err(self):
    with self.assertRaises(ValueError):
      self.node5.to_html()    

  def test_repr(self):
    self.assertEqual(self.node1.__repr__(), self.node1_repr)
    

if __name__ == "__main__":
    unittest.main()
