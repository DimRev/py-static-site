from parentnode import ParentNode
from to_nodes import text_to_textnodes, text_node_to_html_node

def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(markdown)
  children_nodes = []
  for block in blocks:
    block_type = block_to_block_type(block)
    if block_type == "heading 1":
      children_nodes.append(block_to_heading_node(block, 1))
    elif block_type == "heading 2":
      children_nodes.append(block_to_heading_node(block, 2))
    elif block_type == "heading 3":
      children_nodes.append(block_to_heading_node(block, 3))
    elif block_type == "heading 4":
      children_nodes.append(block_to_heading_node(block, 4))
    elif block_type == "heading 5":
      children_nodes.append(block_to_heading_node(block, 5))
    elif block_type == "heading 6":
      children_nodes.append(block_to_heading_node(block, 6))
    elif block_type == "code":
      children_nodes.append(block_to_code_node(block))
    elif block_type == "unordered list":
      children_nodes.append(block_to_list_node(block, "ul"))
    elif block_type == "ordered list":
      children_nodes.append(block_to_list_node(block, "ol"))
    elif block_type == "quote block":
      children_nodes.append(block_to_blockquote_node(block))
    elif block_type == "paragraph":
      children_nodes.append(block_to_paragraph_node(block))
    else:
      raise Exception("block type not supported")
  div_node = ParentNode("div", children_nodes)
  return div_node

def block_to_heading_node(block, level):
  remove_prefix = block[level + 1:]
  children_text_nodes = text_to_textnodes(remove_prefix)
  children_html_nodes = list(map(lambda text_node: text_node_to_html_node(text_node), children_text_nodes))
  heading_html = ParentNode(f"h{level}",children_html_nodes)
  return heading_html

def block_to_code_node(block):
  remove_prefix = block[3:-3]
  children_text_nodes = text_to_textnodes(remove_prefix)
  children_html_nodes = list(map(lambda text_node: text_node_to_html_node(text_node), children_text_nodes))
  code_html = ParentNode("pre",children_html_nodes)
  return code_html

def block_to_list_node(block, node_type):
  lines = block.split("\n")
  lines_html_nodes = [] 
  for line in lines:
    remove_prefix = line[2:] if node_type == "ul" else line[3:]
    children_text_nodes = text_to_textnodes(remove_prefix)
    children_html_nodes = list(map(lambda text_node: text_node_to_html_node(text_node), children_text_nodes))
    parent_node = ParentNode("li", children_html_nodes)
    lines_html_nodes.append(parent_node)
  list_html = ParentNode(node_type, lines_html_nodes)
  return list_html

def block_to_blockquote_node(block):
  lines = block.split("\n")
  remove_prefix = list(map(lambda line: line[2:], lines))
  formatted_blocks = "\n".join(remove_prefix)
  children_text_nodes = text_to_textnodes(formatted_blocks)
  parent_node = list(map(lambda text_node: text_node_to_html_node(text_node), children_text_nodes))
  quote_html = ParentNode("blockquote", parent_node)
  return quote_html
  

def block_to_paragraph_node(block):
  children_text_nodes = text_to_textnodes(block)
  children_html_nodes = list(map(lambda text_node: text_node_to_html_node(text_node), children_text_nodes))
  paragraph_html = ParentNode("p",children_html_nodes)
  return paragraph_html

def block_to_block_type(block):
  if block == "":
    raise ValueError("can't parse empty block")
  elif block.startswith("###### "):
    return "heading 6"
  elif block.startswith("##### "):
    return "heading 5"
  elif block.startswith("#### "):
    return "heading 4"
  elif block.startswith("### "):
    return "heading 3"
  elif block.startswith("## "):
    return "heading 2"
  elif block.startswith("# "):
    return "heading 1"
  elif block.startswith("```\n") and block.endswith("\n```"):
    return "code"

  lines = list(filter(lambda line: line != "",block.split("\n")))

  if all(line.startswith("* ") for line in lines):
    return "unordered list"
  
  if all(line.startswith("- ") for line in lines):
    return "unordered list"

  if all(line.startswith(str(i) + ". ") for i, line in enumerate(lines, 1)):
        return "ordered list"
      
  if all(line.startswith("> ") for line in lines):
    return "quote block"

  return "paragraph"  

def markdown_to_blocks(mdText):
  blocks = mdText.strip().split('\n\n')
  filtered_blocks = list(filter(lambda block: block != "", blocks))
  stripped_blocks = list(map(lambda block: block.strip(), filtered_blocks))
  return stripped_blocks