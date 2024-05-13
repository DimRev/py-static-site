import os
from mkdn_parse import markdown_to_html_node, markdown_to_blocks


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("#"):
            return block[2:]
    raise Exception("header is required")


def generate_pages(from_paths: str, template_path, from_prefix, dest_prefix):
    for from_path in from_paths:
        to_path = from_path.replace(from_prefix, dest_prefix).replace(".md", ".html")
        file_path = to_path.strip("/index.html")
        os.makedirs(file_path, exist_ok=True)
        generate_page(from_path, template_path, to_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = ""
    template = ""
    try:
        with open(from_path, "r") as file:
            markdown = file.read()
    except FileNotFoundError:
        raise f"Markdown file {from_path} not found"
    except Exception as e:
        raise f"Something went wrong with markdown file: {e}"

    try:
        with open(template_path, "r") as file:
            template = file.read()
    except FileNotFoundError:
        raise f"Template file {template_path} not found"
    except Exception as e:
        raise f"Something went wrong with template file: {e}"

    markdown_html = markdown_to_html_node(markdown)
    title = extract_title(markdown)
    generated_html = template.replace("{{ Title }}", title).replace(
        "{{ Content }}", markdown_html.to_html()
    )

    try:
        with open(dest_path, "w") as file:
            file.write(generated_html)
            print(f"HTML page generated and saved to {dest_path}")
    except Exception as e:
        raise Exception(f"Error writing HTML content to {dest_path}: {e}")
