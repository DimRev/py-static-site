import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node1 = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "bold")
    self.assertEqual(node1, node2)
    
    node3 = TextNode("This is another test node", "italic", None)
    node4 = TextNode("This is another test not equal", "italic", None)
    self.assertNotEqual(node3,node4)
    
    node5 = TextNode("This is another test equal", "bold", None)
    node6 = TextNode("This is another test equal", "italic", None)
    self.assertNotEqual(node5,node6)
    
    node5 = TextNode("This is another test equal", "bold", "https://google.com")
    node6 = TextNode("This is another test equal", "bold", None)
    self.assertNotEqual(node5,node6)


if __name__ == "__main__":
    unittest.main()
