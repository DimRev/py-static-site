from htmlnode import HTMLNode
class ParentNode(HTMLNode):
  def __init__(self, tag, children, props = None):
    super().__init__(tag, None, children, props)
  
  def to_html(self):
    if self.tag is None:
      raise ValueError("Cannot render node with no value")
    
    html = f"<{self.tag}{self.props_to_html()}>"
    for child in self.children:
      html += child.to_html()
    html += f"</{self.tag}>"

    return html
  
  def __repr__(self):
    return f"ParentNode({self.tag},{self.children},{self.props})"
