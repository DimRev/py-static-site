from textnode import TextNode,TextType
from leafnode import LeafNode
from parentnode import ParentNode
import re

def main():
  pass

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

def split_delimiter(old_node: TextNode, delimiter, text_type: TextType):
    text = old_node.text
    text_nodes = []
    blocks = text.split(delimiter)
    
    if len(blocks) == 1 and blocks[0] == "":
      return [old_node]
    if len(blocks) % 2 == 0:
      raise Exception("missing closing delimiter")

    for i, block in enumerate(blocks):
      if i % 2 == 0:  
        if block == "":
          continue
        text_node = TextNode(block, old_node.text_type)
        text_nodes.append(text_node)  
      else:
        text_node = TextNode(block, text_type)    
        text_nodes.append(text_node)
            
    return text_nodes

def split_nodes_image(old_node):
    text = old_node.text
    text_nodes = []
    blocks = re.split(r"(!\[(?:.*?)\]\((?:.*?)\))", text)

    if len(blocks) == 1 and blocks[0] == "":
      return [old_node]

    for i, block in enumerate(blocks):
      if i % 2 == 0:  
        if block == "":
          continue
        text_node = TextNode(block, old_node.text_type)
        text_nodes.append(text_node)  
      else:
        images_tup = extract_markdown_images(block)
        text_node = TextNode(images_tup[0][0], TextType.IMAGE, images_tup[0][1])    
        text_nodes.append(text_node)

    return text_nodes

def split_nodes_links(old_node):
    text = old_node.text
    text_nodes = []
    blocks = re.split(r"(\[(?:.*?)\]\((?:.*?)\))", text)

    if len(blocks) == 1 and blocks[0] == "":
      return [old_node]

    for i, block in enumerate(blocks):
      if i % 2 == 0:  
        if block == "":
          continue
        text_node = TextNode(block, old_node.text_type)
        text_nodes.append(text_node)  
      else:
        images_tup = extract_markdown_links(block)
        text_node = TextNode(images_tup[0][0], TextType.LINK, images_tup[0][1])    
        text_nodes.append(text_node)

    return text_nodes

def extract_markdown_images(text):
  return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
  
  
def extract_markdown_links(text):
  return re.findall(r"\[(.*?)\]\((.*?)\)", text)

main()