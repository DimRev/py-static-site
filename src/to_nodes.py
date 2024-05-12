from textnode import TextNode,TextType
from leafnode import LeafNode
from split import split_delimiter, split_nodes_image, split_nodes_links

def text_to_textnodes(text):
  default_node = TextNode(text, TextType.TEXT)
  
  split_on_bold = split_delimiter(default_node, "**", TextType.BOLD)

  bold_italic = []
  for block in split_on_bold:
    split_on_italic = split_delimiter(block, "*", TextType.ITALIC)
    bold_italic.extend(split_on_italic)

  bold_italic_code = []
  for block in bold_italic:
    split_on_code = split_delimiter(block, "`", TextType.CODE)
    bold_italic_code.extend(split_on_code)

  bold_italic_code_image = []
  for block in bold_italic_code:
    split_on_image = split_nodes_image(block)
    bold_italic_code_image.extend(split_on_image)

  bold_italic_code_image_link = []
  for block in bold_italic_code_image:
    if block.text_type == TextType.IMAGE:
      bold_italic_code_image_link.append(block)  
      continue
    split_on_link = split_nodes_links(block)
    bold_italic_code_image_link.extend(split_on_link)

  
  return bold_italic_code_image_link

def text_node_to_html_node(text_node: TextNode):
  text_type = text_node.text_type
  text = text_node.text
  url = text_node.url
  if text_type == TextType.TEXT:
    return LeafNode(None, text)
  elif text_type == TextType.BOLD:
    return LeafNode("b", text)
  elif text_type == TextType.ITALIC:
    return LeafNode("i", text)
  elif text_type == TextType.CODE:
    return LeafNode("code", text)
  elif text_type == TextType.LINK:
    return LeafNode("a", text, {"href": url})
  elif text_type == TextType.IMAGE:
    return LeafNode("img", None, {"src":url, "alt":text})
  else:
    raise Exception("text type not supported")