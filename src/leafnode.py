from htmlnode import HTMLNode
class LeafNode(HTMLNode):
  def __init__(self, tag, value, props = None):
    super().__init__(tag, value, None, props)
  
  def to_html(self):
    if self.tag == "img":
      if self.value != None:
        raise ValueError("image can not have a value")
      return f"<{self.tag}{self.props_to_html()}/>"
    
    if self.value is None:
      raise ValueError("cannot render node with no value")
    if self.tag is None:
      return self.value

    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

  def __repr__(self):
    return f"LeafNode({self.tag},{self.value},{self.props})"