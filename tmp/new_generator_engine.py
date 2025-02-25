from generator.class_generator import (
    read_all_files_in_directory,
)
import json
import os
import shutil
import re
from typing import Optional, Dict, Any, List, Union
from pydantic import BaseModel, Field


class Generator:
    def __init__(self, name):
        """Initialize the generator with a name."""
        self.name = name

    def __init__(self, name):
        """Initialize the generator with a name."""
        self.name = name

    def generate(self, config_path):
        self.remove_trigger_tools("src/agentic_tools/tools/generated")
        self.generate_classes_from_config(
            config_path, "src/agentic_tools/tools/generated"
        )
        # After generating all the tools, create the Langchain toolkit
        self.create_langchain_toolkit("src/agentic_tools/tools/generated")

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

                # Skip tools with "trigger" in their name
                if "trigger" in tool_name.lower():
                    print(f"Skipping {tool_name} as it contains 'trigger' in its name")
                    continue

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

                # Ensure we have at least one operation
                if not operations:
                    print(
                        f"Warning: No operations found for {tool_name}, adding default operation"
                    )
                    operations = ["default"]

                # Track if any operations were successfully generated
                operations_generated = False

                # Generate a file for each operation
                for operation in operations:
                    try:
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

                        operations_generated = True
                        print(
                            f"Successfully generated operation {operation} for {tool_name}"
                        )
                    except Exception as e:
                        print(
                            f"Error generating operation {operation} for {tool_name}: {str(e)}"
                        )

                # If no operations were generated, create a default one
                if not operations_generated:
                    print(
                        f"No operations were successfully generated for {tool_name}, creating default operation"
                    )
                    try:
                        # Create a simple default operation
                        default_operation = "default"
                        operation_file = self._generate_operation_file(
                            tool_name, default_operation, config
                        )
                        operation_file_path = os.path.join(
                            operations_dir, f"{default_operation.lower()}.py"
                        )
                        with open(operation_file_path, "w") as file:
                            file.write(operation_file)

                        # Add import and tool to the __init__.py file
                        with open(
                            os.path.join(operations_dir, "__init__.py"), "a"
                        ) as init_file:
                            init_file.write(
                                f"    from .{default_operation.lower()} import {tool_name.capitalize()}{default_operation.capitalize()}Tool\n"
                            )
                            init_file.write(
                                f"    tools.append({tool_name.capitalize()}{default_operation.capitalize()}Tool())\n"
                            )

                        operations = [default_operation]
                        print(f"Successfully created default operation for {tool_name}")
                    except Exception as e:
                        print(
                            f"Error creating default operation for {tool_name}: {str(e)}"
                        )
                        # If we can't create any operations, this toolkit will be empty

                # Debug output
                print(
                    f"Generated {len(operations)} operations for {tool_name}: {', '.join(operations)}"
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

    def create_langchain_toolkit(self, generated_dir):
        """Create a Langchain toolkit that imports all generated tools."""
        # Get all directories in the generated directory
        tool_dirs = [
            d
            for d in os.listdir(generated_dir)
            if os.path.isdir(os.path.join(generated_dir, d))
            and "trigger" not in d.lower()
        ]

        # Create or update the __init__.py file in the generated directory
        init_path = os.path.join(generated_dir, "__init__.py")
        with open(init_path, "w") as init_file:
            init_file.write("# Generated tools package\n")
            init_file.write("from typing import List\n")
            init_file.write("from langchain.tools import BaseTool\n\n")

            # Import all toolkit classes
            for tool_dir in tool_dirs:
                # Convert directory name to a valid Python identifier
                tool_name = tool_dir.lower()
                toolkit_class_name = self._get_toolkit_class_name(tool_name)
                init_file.write(f"from .{tool_name} import {toolkit_class_name}\n")

            init_file.write("\n\n# Export all toolkit classes\n")
            init_file.write("__all__ = [\n")
            for tool_dir in tool_dirs:
                tool_name = tool_dir.lower()
                toolkit_class_name = self._get_toolkit_class_name(tool_name)
                init_file.write(f"    '{toolkit_class_name}',\n")
            init_file.write("]\n")

        print(f"Created Langchain toolkit with {len(tool_dirs)} toolkit classes")

        # Update each tool directory to include a toolkit class
        for tool_dir in tool_dirs:
            tool_name = tool_dir.lower()
            toolkit_class_name = self._get_toolkit_class_name(tool_name)

            # Update the __init__.py file in the tool directory
            tool_init_path = os.path.join(generated_dir, tool_dir, "__init__.py")

            # Read the existing content
            with open(tool_init_path, "r") as init_file:
                content = init_file.read()

            # Add the toolkit class if it doesn't exist
            if f"class {toolkit_class_name}" not in content:
                with open(tool_init_path, "w") as init_file:
                    init_file.write(f"# {tool_name} toolkit\n")
                    init_file.write("from langchain.tools import BaseTool\n")
                    init_file.write("from typing import List\n\n")

                    # Add the get_tools function
                    init_file.write(f"def get_{tool_name}_tools() -> List[BaseTool]:\n")
                    init_file.write(f'    """Get all {tool_name} tools."""\n')
                    init_file.write("    from . import operations\n")
                    init_file.write("    return operations.get_tools()\n\n")

                    # Add the toolkit class
                    init_file.write(f"class {toolkit_class_name}:\n")
                    init_file.write(
                        f'    """Toolkit for interacting with {tool_name}."""\n\n'
                    )
                    init_file.write(
                        "    def __init__(self, credentials: Optional[Dict[str, str]] = None):\n"
                    )
                    init_file.write(
                        f'        """Initialize the {tool_name} toolkit with optional credentials.\n\n'
                    )
                    init_file.write("        Args:\n")
                    init_file.write(
                        "            credentials: Dictionary containing authentication credentials like API keys\n"
                    )
                    init_file.write('        """\n')
                    init_file.write(
                        "        self.credentials: Dict[str, str] = credentials or {}\n\n"
                    )
                    init_file.write("    def get_tools(self) -> List[BaseTool]:\n")
                    init_file.write(
                        f'        """Get all {tool_name} tools with the configured credentials."""\n'
                    )
                    init_file.write("        from . import operations\n")
                    init_file.write("        tools = operations.get_tools()\n")
                    init_file.write(
                        "        # Apply credentials to each tool if provided\n"
                    )
                    init_file.write("        if self.credentials:\n")
                    init_file.write("            for tool in tools:\n")
                    init_file.write(
                        "                tool.credentials = self.credentials\n"
                    )
                    init_file.write("        return tools\n\n")
                    init_file.write("    @staticmethod\n")
                    init_file.write("    def get_default_tools() -> List[BaseTool]:\n")
                    init_file.write(
                        f'        """Get all {tool_name} tools with default credentials."""\n'
                    )
                    init_file.write(f"        return get_{tool_name}_tools()\n")

            print(f"Updated {tool_name} with toolkit class {toolkit_class_name}")

        # Update the main tools/__init__.py to import toolkit classes
        main_init_path = os.path.join(os.path.dirname(generated_dir), "__init__.py")
        if os.path.exists(main_init_path):
            with open(main_init_path, "w") as main_init_file:
                main_init_file.write("from .base import *\n")
                main_init_file.write("from .generated import *\n\n")
                main_init_file.write("# Tools package\n")
                main_init_file.write("# Import all toolkit classes from generated\n")
                main_init_file.write("# Usage examples:\n")
                main_init_file.write("# 1. With default credentials:\n")
                main_init_file.write("#    from agentic_tools.tools import S3Toolkit\n")
                main_init_file.write("#    tools = S3Toolkit().get_tools()\n")
                main_init_file.write("#\n")
                main_init_file.write("# 2. With custom credentials:\n")
                main_init_file.write("#    from agentic_tools.tools import S3Toolkit\n")
                main_init_file.write("#    credentials = {\n")
                main_init_file.write(
                    "#        'aws_access_key_id': 'your-access-key',\n"
                )
                main_init_file.write(
                    "#        'aws_secret_access_key': 'your-secret-key',\n"
                )
                main_init_file.write("#        'region_name': 'us-west-2'\n")
                main_init_file.write("#    }\n")
                main_init_file.write(
                    "#    tools = S3Toolkit(credentials=credentials).get_tools()\n"
                )

            print(
                "Updated main tools/__init__.py to import toolkit classes with credential examples"
            )

    def _get_toolkit_class_name(self, tool_name):
        """Convert a tool name to a toolkit class name."""
        # Handle special cases
        if tool_name.startswith("aws"):
            # For AWS services, use format like AwsS3Toolkit
            parts = tool_name.split("aws")
            if len(parts) > 1 and parts[1]:
                return f"Aws{parts[1].capitalize()}Toolkit"

        # For other tools, capitalize each word and add Toolkit
        words = re.findall(r"[a-zA-Z][a-z]*", tool_name)
        return "".join(word.capitalize() for word in words) + "Toolkit"

    def _extract_operations(self, config):
        """Extract operations from the config."""
        operations = []

        # Look for operation property in the config
        input_schema = config.get("init_kwargs", {}).get("input_desc", {})
        if not input_schema:
            print(f"Warning: No input_desc found in config, using default operation")
            return ["default"]

        operation_prop = input_schema.get("properties", {}).get("operation", {})
        if not operation_prop:
            print(
                f"Warning: No operation property found in config, using default operation"
            )
            return ["default"]

        print(f"Found operation property: {operation_prop}")

        # Try to extract operations from different formats
        if "anyOf" in operation_prop:
            for op_option in operation_prop["anyOf"]:
                if "enum" in op_option:
                    operations.extend(op_option["enum"])
                    print(f"Found operations in anyOf enum: {op_option['enum']}")
        elif "enum" in operation_prop:
            operations.extend(operation_prop["enum"])
            print(f"Found operations in enum: {operation_prop['enum']}")
        elif "type" in operation_prop and operation_prop["type"] == "string":
            # If operation is a string type without enum, use the property name
            operations = ["default"]
            print("Operation is string type without enum, using default")

        # If still no operations found, check if there are any other properties that might indicate operations
        if not operations:
            # Look for properties with displayOptions that might indicate operations
            for prop_name, prop_details in input_schema.get("properties", {}).items():
                if (
                    "displayOptions" in prop_details
                    and "show" in prop_details["displayOptions"]
                ):
                    show_options = prop_details["displayOptions"]["show"]
                    if "operation" in show_options:
                        potential_ops = show_options["operation"]
                        if isinstance(potential_ops, list):
                            for op in potential_ops:
                                if op not in operations:
                                    operations.append(op)
                            print(
                                f"Found operations in displayOptions: {potential_ops}"
                            )

        # If still no operations found, use a default one
        if not operations:
            operations = ["default"]
            print("No operations found, using default")

        print(f"Final operations list: {operations}")
        return operations

    def _camel_to_snake(self, name):
        """Convert camelCase to snake_case."""
        # Add underscore before each uppercase letter and convert to lowercase
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

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
    # Allow users to provide their own credentials
    credentials: Optional[Dict[str, str]] = Field(None, description="Custom credentials for authentication (e.g., {'api_key': 'your-key', 'secret': 'your-secret'})")

"""

        # Generate the input fields relevant to this operation
        properties = input_schema.get("properties", {})
        for prop_name, prop_details in properties.items():
            # Skip credentials as we've already added it
            if prop_name in ["load_files"]:
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

            # Convert camelCase property name to snake_case
            snake_case_prop_name = self._camel_to_snake(prop_name)

            # Add the field to the class
            class_definition += f'    {snake_case_prop_name}: Optional[{python_type}] = Field(None, description="{description_text}")\n'

        # Add the tool class
        class_definition += f"""

class {class_name}(BaseTool):
    name = "{tool_name.lower()}_{operation.lower()}"
    description = "{description} - {operation} operation"
    
    def __init__(self, credentials: Optional[Dict[str, str]] = None, **kwargs):
        \"\"\"Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Dictionary containing authentication credentials
            **kwargs: Additional keyword arguments
        \"\"\"
        super().__init__(**kwargs)
        self.credentials: Dict[str, str] = credentials or {{}}
    
    def _run(self, **kwargs):
        \"\"\"Run the {tool_name} {operation} operation.\"\"\"
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = {{k: "***" for k in credentials.keys()}}
            return f"Running {tool_name} {operation} operation with custom credentials {{safe_credentials}} and args: {{kwargs}}"
        else:
            return f"Running {tool_name} {operation} operation with default credentials and args: {{kwargs}}"
    
    async def _arun(self, **kwargs):
        \"\"\"Run the {tool_name} {operation} operation asynchronously.\"\"\"
        # Implement the async tool logic here
        return self._run(**kwargs)
"""

        return class_definition

    def _is_property_relevant_for_operation(self, prop_details, operation):
        """Check if a property is relevant for a specific operation."""
        # If property details is None or not a dict, assume it's relevant
        if not prop_details or not isinstance(prop_details, dict):
            return True

        # If no displayOptions, assume it's relevant for all operations
        if "displayOptions" not in prop_details:
            return True

        # Check if the operation is in the displayOptions
        display_options = prop_details.get("displayOptions", {})
        if "show" not in display_options:
            return True

        show_options = display_options.get("show", {})

        # Handle different formats of operation specification
        if "operation" in show_options:
            operations = show_options.get("operation", [])

            # Handle string operation
            if isinstance(operations, str):
                return operations == operation

            # Handle list of operations
            elif isinstance(operations, list):
                return operation in operations

            # Handle dict with operation as key
            elif isinstance(operations, dict) and operation in operations:
                return True

            # If operation is specified but doesn't match any format, assume not relevant
            return False

        # If operation is not specified in show options, check if there's a condition
        # that might be related to the operation
        for key, value in show_options.items():
            # If there's a condition that matches the operation name, assume it's relevant
            if key == operation or (
                isinstance(value, (list, str)) and operation in value
            ):
                return True

        # If no operation specified in displayOptions, assume it's relevant
        return True

    def remove_trigger_tools(self, generated_dir):
        """Remove all tools with 'trigger' in their name."""
        if not os.path.exists(generated_dir):
            return

        # Get all directories in the generated directory
        tool_dirs = [
            d
            for d in os.listdir(generated_dir)
            if os.path.isdir(os.path.join(generated_dir, d))
        ]

        # Remove directories with 'trigger' in their name
        for tool_dir in tool_dirs:
            if "trigger" in tool_dir.lower():
                dir_path = os.path.join(generated_dir, tool_dir)
                print(f"Removing trigger tool: {tool_dir}")
                shutil.rmtree(dir_path)


if __name__ == "__main__":
    # Example usage of the Generator class
    import os

    root_path = os.path.dirname(os.path.abspath(__file__)) + "../"
    generator = Generator("Example")
    generator.generate(os.path.join(root_path, "engine_config"))
