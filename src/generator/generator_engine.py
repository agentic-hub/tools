from generator.class_generator import (
    read_all_files_in_directory,
)
import json
import os
import shutil
import re


class Generator:
    def __init__(self, name):
        """Initialize the generator with a name."""
        self.name = name

    def generate(self, config_path):
        self.generate_classes_from_config(
            config_path, "src/agentic_tools/tools/generated"
        )

    def generate_classes_from_config(self, config_path, output_directory):
        """Generate classes from a configuration file."""
        configs = read_all_files_in_directory(config_path)

        # Create the output directory if it doesn't exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        for filename, config_str in configs.items():
            try:
                config = json.loads(config_str)
                tool_name = filename.split(".")[
                    1
                ]  # Extract the tool name from the filename

                # Create a directory for this tool
                tool_dir = os.path.join(output_directory, tool_name.lower())

                # Delete the directory if it exists
                if os.path.exists(tool_dir):
                    shutil.rmtree(tool_dir)

                # Create the directory
                os.makedirs(tool_dir)

                # Create an __init__.py file in the tool directory
                with open(os.path.join(tool_dir, "__init__.py"), "w") as init_file:
                    init_file.write(f"# {tool_name} toolkit\n")
                    init_file.write("from langchain.tools import BaseTool\n")
                    init_file.write("from typing import List\n\n")
                    init_file.write(
                        f"def get_{tool_name.lower()}_tools() -> List[BaseTool]:\n"
                    )
                    init_file.write(f'    """Get all {tool_name} tools."""\n')
                    init_file.write("    from . import operations\n")
                    init_file.write("    return operations.get_tools()\n")

                # Create operations directory
                operations_dir = os.path.join(tool_dir, "operations")
                os.makedirs(operations_dir)

                # Create an __init__.py file in the operations directory
                with open(
                    os.path.join(operations_dir, "__init__.py"), "w"
                ) as init_file:
                    init_file.write(f"# {tool_name} operations\n")
                    init_file.write("from typing import List\n")
                    init_file.write("from langchain.tools import BaseTool\n\n")
                    init_file.write("def get_tools() -> List[BaseTool]:\n")
                    init_file.write(f'    """Get all {tool_name} operation tools."""\n')
                    init_file.write("    tools = []\n")

                # Extract operations from the config
                operations = self._extract_operations(config)

                # Generate a file for each operation
                for operation in operations:
                    operation_file = self._generate_operation_file(
                        tool_name, operation, config
                    )
                    operation_file_path = os.path.join(
                        operations_dir, f"{operation.lower()}.py"
                    )
                    with open(operation_file_path, "w") as file:
                        file.write(operation_file)

                    # Add import and tool to the __init__.py file
                    with open(
                        os.path.join(operations_dir, "__init__.py"), "a"
                    ) as init_file:
                        init_file.write(
                            f"    from .{operation.lower()} import {tool_name.capitalize()}{operation.capitalize()}Tool\n"
                        )
                        init_file.write(
                            f"    tools.append({tool_name.capitalize()}{operation.capitalize()}Tool())\n"
                        )

                # Close the get_tools function
                with open(
                    os.path.join(operations_dir, "__init__.py"), "a"
                ) as init_file:
                    init_file.write("    return tools\n")

                print(
                    f"Generated toolkit for {tool_name} with {len(operations)} operations"
                )

            except json.JSONDecodeError:
                print(f"Error parsing JSON from {filename}")
            except Exception as e:
                print(f"Error generating toolkit from {filename}: {str(e)}")

    def _extract_operations(self, config):
        """Extract operations from the config."""
        operations = []

        # Look for operation property in the config
        input_schema = config.get("init_kwargs", {}).get("input_desc", {})
        operation_prop = input_schema.get("properties", {}).get("operation", {})

        if "anyOf" in operation_prop:
            for op_option in operation_prop["anyOf"]:
                if "enum" in op_option:
                    operations.extend(op_option["enum"])
        elif "enum" in operation_prop:
            operations.extend(operation_prop["enum"])

        # If no operations found, use a default one
        if not operations:
            operations = ["default"]

        return operations

    def _generate_operation_file(self, tool_name, operation, config):
        """Generate a file for a specific operation."""
        class_name = f"{tool_name.capitalize()}{operation.capitalize()}Tool"

        # Extract the description from the config
        description = config.get(
            "description", f"Tool for {tool_name} {operation} operation"
        )

        # Extract the input schema from the config
        input_schema = config.get("init_kwargs", {}).get("input_desc", {})

        # Generate the class definition
        class_definition = f"""from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class {class_name}Input(BaseModel):
"""

        # Generate the input fields relevant to this operation
        properties = input_schema.get("properties", {})
        for prop_name, prop_details in properties.items():
            # Skip certain properties that are not relevant for the tool
            if prop_name in ["credentials", "load_files"]:
                continue

            # Check if this property is relevant for this operation
            if not self._is_property_relevant_for_operation(prop_details, operation):
                continue

            # Handle anyOf properties
            if "anyOf" in prop_details:
                # Find the option relevant to this operation
                for option in prop_details["anyOf"]:
                    if self._is_property_relevant_for_operation(option, operation):
                        prop_details = option
                        break
                else:
                    # If no relevant option found, use the first one
                    prop_details = prop_details["anyOf"][0]

            # Get the property type
            prop_type = prop_details.get("type", "string")

            # Map JSON schema types to Python types
            type_mapping = {
                "string": "str",
                "integer": "int",
                "number": "float",
                "boolean": "bool",
                "array": "List[Any]",
                "object": "Dict[str, Any]",
            }
            python_type = type_mapping.get(prop_type, "Any")

            # Get the description
            description_text = prop_details.get("description", "")
            if not description_text:
                description_text = prop_details.get("title", prop_name)

            # Escape quotes in description
            description_text = description_text.replace('"', '\\"')

            # Add the field to the class
            class_definition += f'    {prop_name}: Optional[{python_type}] = Field(None, description="{description_text}")\n'

        # Add the tool class
        class_definition += f"""

class {class_name}(BaseTool):
    name = "{tool_name.lower()}_{operation.lower()}"
    description = "{description} - {operation} operation"
    
    def _run(self, **kwargs):
        \"\"\"Run the {tool_name} {operation} operation.\"\"\"
        # Implement the tool logic here
        return f"Running {tool_name} {operation} operation with args: {{kwargs}}"
    
    async def _arun(self, **kwargs):
        \"\"\"Run the {tool_name} {operation} operation asynchronously.\"\"\"
        # Implement the async tool logic here
        return self._run(**kwargs)
"""

        return class_definition

    def _is_property_relevant_for_operation(self, prop_details, operation):
        """Check if a property is relevant for a specific operation."""
        # If no displayOptions, assume it's relevant for all operations
        if "displayOptions" not in prop_details:
            return True

        # Check if the operation is in the displayOptions
        display_options = prop_details.get("displayOptions", {})
        if "show" not in display_options:
            return True

        show_options = display_options.get("show", {})
        if "operation" in show_options:
            operations = show_options.get("operation", [])
            if isinstance(operations, list) and operation in operations:
                return True
            return False

        # If no operation specified in displayOptions, assume it's relevant
        return True


if __name__ == "__main__":
    # Example usage of the Generator class
    import os

    root_path = os.path.dirname(os.path.abspath(__file__))
    generator = Generator("Example")
    generator.generate(os.path.join(root_path, "engine_config"))
