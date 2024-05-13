import re
from generate import generate_page
from copyfiles import clean_directory, get_file_paths, copy_files, create_folders


def main():
    file_paths = get_file_paths("./static/")
    clean_directory("./public/")
    copy_files(file_paths, "./static/", "./public/")
    generate_page("./content/index.md", "./template.html", "./public/index.html")


main()
