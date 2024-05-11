import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
  def __init__(self, methodName: str = "runTest") -> None:
    super().__init__(methodName)
    self.node1 = TextNode("This is a text node", "bold")
    self.node2 = TextNode("This is a text node", "bold")
    
    self.node3 = TextNode("This is another test node", "italic", None)
    self.node4 = TextNode("This is another test not equal", "italic", None)
    
    self.node5 = TextNode("This is another test equal", "bold", None)
    self.node6 = TextNode("This is another test equal", "italic", None)
    
    self.node5 = TextNode("This is another test equal", "bold", "https://google.com")
    self.node6 = TextNode("This is another test equal", "bold", None)

  def test_partially_def_eq(self):
    self.assertEqual(self.node1, self.node2)
    
  def test_text_mismatch_eq(self):  
    self.assertNotEqual(self.node3,self.node4)
    
  def test_text_type_mismatch_eq(self):  
    self.assertNotEqual(self.node5,self.node6)
    
  def test_url_mismatch_eq(self):  
    self.assertNotEqual(self.node5,self.node6)


if __name__ == "__main__":
    unittest.main()
