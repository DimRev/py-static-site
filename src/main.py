import re
from generate import generate_pages
from copyfiles import (
    clean_directory,
    get_file_paths,
    copy_files,
)


def main():
    file_paths = get_file_paths("./static/")
    clean_directory("./public/")
    copy_files(file_paths, "./static/", "./public/")
    markdown_paths = get_file_paths("./content/")
    ("./content/index.md", "./template.html", "./public/index.html")
    generate_pages(markdown_paths, "./template.html", "./content/", "./public/")


main()
