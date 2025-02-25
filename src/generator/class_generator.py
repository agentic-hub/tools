import json
import os


def read_all_files_in_directory(directory_path):
    """Read all files in the specified directory and return their contents."""
    file_contents = {}
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                file_contents[filename] = file.read()
    return file_contents
