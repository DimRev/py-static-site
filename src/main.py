import re

from textnode import TextNode,TextType
from leafnode import LeafNode
from parentnode import ParentNode
from mkdn_parse import markdown_to_html_node

def main():
  markdown = '''
# Heading 1 test

* 1 
* 2
* 3
  '''
  html_node = markdown_to_html_node(markdown)
  print(html_node.to_html())






main()