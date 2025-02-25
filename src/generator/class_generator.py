import json
import os


# def parse_engine_config(config_path):
#     """Parse the engine configuration file."""
#     with open(config_path, "r") as file:
#         return json.load(file)


# def create_class(name, attributes):
#     """Create a class definition from a name and attributes."""
#     class_definition = f"class {name}:\n"
#     class_definition += "    def __init__(self, " + ", ".join(attributes) + "):\n"
#     for attr in attributes:
#         class_definition += f"        self.{attr} = {attr}\n"
#     return class_definition


# def write_class_to_file(class_name, class_definition, directory):
#     """Write the class definition to a file."""
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#     file_path = os.path.join(directory, f"{class_name}.py")
#     with open(file_path, "w") as file:
#         file.write(class_definition)


def read_all_files_in_directory(directory_path):
    """Read all files in the specified directory and return their contents."""
    file_contents = {}
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                file_contents[filename] = file.read()
    return file_contents
