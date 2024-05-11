import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
  def __init__(self, methodName: str = "runTest") -> None:
    super().__init__(methodName)
    self.child_node1 = LeafNode(None, "Click")
    self.child_node2 = LeafNode("a", "this", {"href":"https://google.com","target":"_blank"})
    self.child_node3 = LeafNode(None, "Link")

    self.parent_node1 = ParentNode("p", [self.child_node1, self.child_node2, self.child_node3])
    self.parent_node2 = ParentNode("p", [self.child_node1, self.child_node2, self.child_node3])
    self.parent_node1_expected = "<p>Click<a href=\"https://google.com\" target=\"_blank\">this</a>Link</p>"

    self.parent_node3 = ParentNode(None, [self.child_node1, self.child_node2, self.child_node3])

    self.empty_parent = ParentNode("div", [])
    self.empty_parent_expected_html = "<div></div>"

    self.node_with_empty_props = LeafNode("span", "Text", {})
    self.node_with_empty_props_expected = ""
    
    self.node_with_none_props = LeafNode("span", "Text", None)
    self.node_with_none_props_expected = ""

    self.nested_parent1 = ParentNode("div", [self.child_node1, self.child_node2])
    self.nested_parent2 = ParentNode("div", [self.nested_parent1, self.child_node3])
    self.nested_parent_expected_html = "<div><div>Click<a href=\"https://google.com\" target=\"_blank\">this</a></div>Link</div>"
    
  def test_fully_def_eq(self):
    self.assertEqual(self.parent_node1, self.parent_node2)

  def test_to_html_method(self):
    self.assertEqual(self.parent_node1.to_html(), self.parent_node1_expected)

  def test_to_html_no_tag_val_err(self):
    with self.assertRaises(ValueError):
      self.parent_node3.to_html()

  def test_empty_children_to_html(self):    
    self.assertEqual(self.empty_parent.to_html(), self.empty_parent_expected_html)

  def test_empty_props_to_html(self):
    self.assertEqual(self.node_with_empty_props.props_to_html(), self.node_with_empty_props_expected)

  def test_none_props_to_html(self):
    self.assertEqual(self.node_with_none_props.props_to_html(), self.node_with_none_props_expected)

  def test_multiple_nested_parents_to_html(self):
    self.assertEqual(self.nested_parent2.to_html(), self.nested_parent_expected_html)

if __name__ == "__main__":
    unittest.main()
