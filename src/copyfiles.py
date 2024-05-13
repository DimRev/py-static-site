import os
import shutil
from typing import List


def get_file_paths(directory: str) -> List[str]:
    """Recursively get all file paths in the specified directory."""
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


def clean_directory(directory: str):
    """Remove all files and subdirectories in the specified directory."""
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)


def copy_files(files: List[str], from_directory: str, to_directory: str):
    """Copy files from from_directory to to_directory, preserving the directory structure."""
    for file in files:

        relative_path = os.path.relpath(file, from_directory)
        to_path = os.path.join(to_directory, relative_path)
        os.makedirs(os.path.dirname(to_path), exist_ok=True)
        shutil.copy2(file, to_path)
        print(f"Copied {file} to {to_path}")


def create_folders(files: List[str], from_directory: str, to_directory: str):
    """Create folders in to_directory based on the directory structure of files."""
    for file in files:
        relative_path = os.path.relpath(file, from_directory)
        dir_path = os.path.dirname(os.path.join(to_directory, relative_path))
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created folder: {dir_path}")
