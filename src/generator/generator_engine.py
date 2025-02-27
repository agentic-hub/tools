from generator.class_generator import (
    read_all_files_in_directory,
)
import json
import os
import shutil
import re
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

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
        self.tool_configs = {}  # Store configs by tool name

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
        self.tool_configs = {}  # Reset tool configs

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

                # Store the config for this tool
                self.tool_configs[tool_name.lower()] = config

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
                    init_file.write(
                        "from agentic_tools.tools import BaseTool, BaseModel, Field\n"
                    )
                    init_file.write("from typing import List, Optional, Dict, Any\n")
                    init_file.write("from .operations import get_tools\n\n")

                    # Generate the credentials class
                    credentials_class = self._generate_credentials_class(
                        tool_name, config
                    )
                    if credentials_class:
                        init_file.write(f"{credentials_class}\n")

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
                    init_file.write(
                        "from agentic_tools.tools import BaseTool, BaseModel\n"
                    )

                    # Import credentials class if available
                    credentials_class = self._generate_credentials_class(
                        tool_name, config
                    )
                    if credentials_class:
                        init_file.write(
                            f"from .. import {tool_name.capitalize()}Credentials\n"
                        )

                    init_file.write("\ndef get_tools() -> List[BaseTool]:\n")
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
                        # Create tool instance without credentials - they will be added by the toolkit
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

    def create_langchain_toolkit(self, generated_dir):
        """Create a Langchain toolkit that imports all generated tools."""
        # Get all directories in the generated directory
        tool_dirs = [
            d
            for d in os.listdir(generated_dir)
            if os.path.isdir(os.path.join(generated_dir, d))
            and ("trigger" not in d.lower() and "__pycache__" not in d.lower())
        ]

        # Create or update the __init__.py file in the generated directory
        init_path = os.path.join(generated_dir, "__init__.py")
        # with open(init_path, "w") as init_file:
        #     init_file.write("# Generated tools package\n")
        #     init_file.write("from typing import List\n")
        #     init_file.write(
        #         "from agentic_tools.tools import BaseTool, BaseModel, Field\n\n"
        #     )

        #     # Import all toolkit classes
        #     for tool_dir in tool_dirs:
        #         # Convert directory name to a valid Python identifier
        #         tool_name = tool_dir.lower()
        #         toolkit_class_name = self._get_toolkit_class_name(tool_name)
        #         init_file.write(f"from .{tool_name} import {toolkit_class_name}\n")

        #     init_file.write("\n\n# Export all toolkit classes\n")
        #     init_file.write("__all__ = [\n")
        #     for tool_dir in tool_dirs:
        #         tool_name = tool_dir.lower()
        #         toolkit_class_name = self._get_toolkit_class_name(tool_name)
        #         init_file.write(f"    '{toolkit_class_name}',\n")
        #     init_file.write("]\n")

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
                    init_file.write(
                        "from agentic_tools.tools import BaseTool, BaseModel, Field\n"
                    )
                    init_file.write(
                        "from agentic_tools.toolkit import AgenticHubToolkit\n"
                    )
                    init_file.write("from typing import List, Optional, Dict, Any\n\n")

                    # Add the get_tools function
                    init_file.write(f"def get_{tool_name}_tools() -> List[BaseTool]:\n")
                    init_file.write(f'    """Get all {tool_name} tools."""\n')
                    init_file.write("    from . import operations\n")
                    init_file.write("    return operations.get_tools()\n\n")

                    # Check if this tool has credentials
                    config = self.tool_configs.get(tool_name.lower(), {})
                    credentials_class = self._generate_credentials_class(
                        tool_name, config
                    )
                    has_credentials = credentials_class is not None

                    # Add the credentials class if available
                    if has_credentials:
                        init_file.write(f"{credentials_class}\n")

                    # Add the toolkit class
                    init_file.write(f"class {toolkit_class_name}(AgenticHubToolkit):\n")
                    init_file.write(
                        f'    """Toolkit for interacting with {tool_name}."""\n\n'
                    )

                    if has_credentials:
                        init_file.write(
                            f"    def __init__(self, credentials: Optional[{tool_name.capitalize()}Credentials] = None):\n"
                        )
                        init_file.write(
                            f'        """Initialize the {tool_name} toolkit with optional credentials.\n\n'
                        )
                        init_file.write("        Args:\n")
                        init_file.write(
                            f"            credentials: {tool_name.capitalize()}Credentials object containing authentication credentials\n"
                        )
                        init_file.write('        """\n')
                        init_file.write("        self.credentials = credentials\n\n")
                    else:
                        init_file.write("    def __init__(self):\n")
                        init_file.write(
                            f'        """Initialize the {tool_name} toolkit."""\n\n'
                        )

                    init_file.write("    def get_tools(self) -> List[BaseTool]:\n")
                    init_file.write(
                        f'        """Get all {tool_name} tools with the configured credentials."""\n'
                    )
                    init_file.write("        from . import operations\n")
                    init_file.write(
                        "        return self.get_tools_from_operations(operations)\n"
                    )

                    if has_credentials:
                        init_file.write(
                            "        # Apply credentials to each tool if provided\n"
                        )
                        init_file.write("        if self.credentials:\n")
                        init_file.write("            for tool in tools:\n")
                        init_file.write(
                            "                # Set credentials on each tool instance\n"
                        )
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
                main_init_file.write(
                    "#    from agentic_tools.tools import S3Toolkit, S3Credentials\n"
                )
                main_init_file.write("#    credentials = S3Credentials(\n")
                main_init_file.write("#        aws_access_key_id='your-access-key',\n")
                main_init_file.write(
                    "#        aws_secret_access_key='your-secret-key',\n"
                )
                main_init_file.write("#        region_name='us-west-2'\n")
                main_init_file.write("#    )\n")
                main_init_file.write(
                    "#    tools = S3Toolkit(credentials=credentials).get_tools()\n"
                )
                main_init_file.write("#\n")
                main_init_file.write("# 3. Using with LangChain:\n")
                main_init_file.write(
                    "#    from langchain.agents import initialize_agent\n"
                )
                main_init_file.write("#    from langchain.llms import OpenAI\n")
                main_init_file.write("#    from agentic_tools.tools import S3Toolkit\n")
                main_init_file.write("#\n")
                main_init_file.write("#    llm = OpenAI(temperature=0)\n")
                main_init_file.write("#    tools = S3Toolkit().get_tools()\n")
                main_init_file.write(
                    "#    agent = initialize_agent(tools, llm, agent='zero-shot-react-description')\n"
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

    def _camel_to_snake(self, name):
        """Convert camelCase to snake_case."""
        # Add underscore before each uppercase letter and convert to lowercase
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

    def _generate_credentials_class(self, tool_name, config):
        """Generate a credentials class from the config schema."""
        # Look for credentials schema in the config
        credentials_schema = {}
        input_schema = config.get("init_kwargs", {}).get("input_desc", {})
        properties = input_schema.get("properties", {})

        # Check if there's a credentials property with schema information
        if "credentials" in properties and "properties" in properties["credentials"]:
            credentials_schema = properties["credentials"]["properties"]

        # If no specific credentials schema found, return None
        if not credentials_schema:
            return None

        # Generate the credentials class
        class_definition = f"""class {tool_name.capitalize()}Credentials(BaseModel):
    \"\"\"Credentials for {tool_name} authentication.\"\"\"
"""

        # Add fields from the schema
        for prop_name, prop_details in credentials_schema.items():
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

        return class_definition

    def _generate_operation_file(self, tool_name, operation, config):
        """Generate a file for a specific operation."""
        class_name = f"{tool_name.capitalize()}{operation.capitalize()}Tool"

        # Extract the description from the config
        description = config.get(
            "description", f"Tool for {tool_name} {operation} operation"
        )
        connector_id = (
            config.get("init_kwargs", {})
            .get("scade_tools_node_name", "")
            .replace("scade-tools-", "")
        )
        # Extract the input schema from the config
        input_schema = config.get("init_kwargs", {}).get("input_desc", {})

        # Generate the credentials class
        credentials_class = self._generate_credentials_class(tool_name, config)
        has_credentials = credentials_class is not None

        # Generate the class definition
        class_definition = f"""from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

"""
        # Add credentials class import if available
        if has_credentials:
            class_definition += (
                f"from .. import {tool_name.capitalize()}Credentials\n\n"
            )

        class_definition += f"""class {class_name}Input(BaseModel):
"""
        # Remove credentials field from InputParams - it will be in the constructor instead

        # Generate the input fields relevant to this operation
        properties = input_schema.get("properties", {})
        for prop_name, prop_details in properties.items():
            # Skip credentials and load_files
            if prop_name.lower() in ["load_files", "credentials"]:
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
    name: str = "{tool_name.lower()}_{operation.lower()}"
    connector_id: str = "{connector_id}"
    description: str = "{description} - {operation} operation"
    args_schema: type[BaseModel] | None = {class_name}Input
"""

        # Add credentials handling if needed
        if has_credentials:
            class_definition += f"""    credentials: Optional[{tool_name.capitalize()}Credentials] = None
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

    root_path = os.getcwd()
    generator = Generator("Example")
    generator.generate(os.path.join(root_path, "src/generator/engine_config"))
