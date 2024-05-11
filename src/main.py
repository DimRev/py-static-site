from textnode import TextNode
from leafnode import LeafNode

def main():
  url_link = TextNode("This is a text node", "bold", "https://boot.dev")
  img = TextNode("Test", "image", "http://example.com")
  img_node = text_node_to_html_node(img)
  print(img_node.to_html())

def text_node_to_html_node(text_node: TextNode):
  text_type = text_node.text_type
  text = text_node.text
  url = text_node.url
  if text_type == 'text':
    return LeafNode(None, text)
  elif text_type == 'bold':
    return LeafNode("b", text)
  elif text_type == 'italic':
    return LeafNode("i", text)
  elif text_type == 'code':
    return LeafNode("code", text)
  elif text_type == 'link':
    return LeafNode("a", text, {"href": url})
  elif text_type == 'image':
    return LeafNode("img", None, {"src":url, "alt":text})
  else:
    raise Exception("text type not supported")

main()