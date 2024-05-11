import unittest

from htmlnode import HTMLNode


class TextHTMLNode(unittest.TestCase):
  def __init__(self, methodName: str = "runTest") -> None:
    super().__init__(methodName)
    self.node1 = HTMLNode("p","Hello world",None,None)
    self.node2 = HTMLNode("p","Hello world",None,None)
    
    self.node3 = HTMLNode("p","Hello world",[self.node1,self.node2],{"data":"random"})
    self.node4 = HTMLNode("p","Hello world",[self.node1,self.node2],{"data":"random"})
    
    self.node5 = HTMLNode("p","Hello world",[self.node1,self.node3],None)
    self.node6 = HTMLNode("p","Hello world",[self.node1,self.node2],None)
    
    self.node7 = HTMLNode("p","Hello world",None,{"data":"random"})
    self.node8 = HTMLNode("p","Hello world",None,{"data":"random2"})
    
    self.node9 = HTMLNode("a", "link to url", None, {"href":"http:/boot.dev", "target": "_blank"})
    self.node9_expected = " href=\"http:/boot.dev\" target=\"_blank\""
    
  def test_partially_def_eq(self):
    self.assertEqual(self.node1, self.node2)

  def test_fully_def_eq(self):
    self.assertEqual(self.node3, self.node4)

  def test_children_mismatch_eq(self):
    self.assertNotEqual(self.node5, self.node6)

  def test_prop_mismatch_eq(self):
    self.assertNotEqual(self.node7, self.node8)

  def test_props_to_html_method(self):
    self.assertEqual(self.node9.props_to_html(), self.node9_expected)
    


if __name__ == "__main__":
    unittest.main()
