import unittest

from htmlnode import HTMLNode


class TextHTMLNode(unittest.TestCase):
  def test_eq(self):
    # Partial defined equal
    node1 = HTMLNode("p","Hello world",None,None)
    node2 = HTMLNode("p","Hello world",None,None)
    self.assertEqual(node1, node2)

    # Fully defined equal
    node3 = HTMLNode("p","Hello world",[node1,node2],{"data":"random"})
    node4 = HTMLNode("p","Hello world",[node1,node2],{"data":"random"})
    self.assertEqual(node3, node4)

    # Children mismatch not equal
    node5 = HTMLNode("p","Hello world",[node1,node3],None)
    node6 = HTMLNode("p","Hello world",[node1,node2],None)
    self.assertNotEqual(node5, node6)

    # Props mismatch not equal
    node7 = HTMLNode("p","Hello world",None,{"data":"random"})
    node8 = HTMLNode("p","Hello world",None,{"data":"random2"})
    self.assertNotEqual(node7, node8)
    
    # props_to_html method
    node9 = HTMLNode("a", "link to url", None, {"href":"http:/boot.dev", "target": "_blank"})
    node9_props_string = " href=\"http:/boot.dev\" target=\"_blank\""
    self.assertEqual(node9.props_to_html(), node9_props_string)
    


if __name__ == "__main__":
    unittest.main()
