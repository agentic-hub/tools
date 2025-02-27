"""Test the generator engine."""

import json
import os
import sys
from typing import Dict, Any

# Add the src directory to the path so we can import the generator module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.generator.generator_engine import Generator


def test_generate_operation_file():
    """Test the _generate_operation_file method."""
    generator = Generator("Test")

    # Create a simple config with credentials
    config = {
        "description": "Test tool",
        "init_kwargs": {
            "input_desc": {
                "properties": {
                    "credentials": {
                        "type": "object",
                        "properties": {
                            "api_key": {"type": "string", "description": "API Key"}
                        },
                    },
                    "param1": {"type": "string", "description": "Parameter 1"},
                    "param2": {"type": "integer", "description": "Parameter 2"},
                }
            }
        },
    }

    # Generate an operation file
    operation_file = generator._generate_operation_file("test", "get", config)

    # Print the operation file
    print(operation_file)

    # Check if credentials are in the InputParams class
    if "credentials: Optional" in operation_file:
        print("ERROR: Credentials are still in the InputParams class!")
    else:
        print("SUCCESS: Credentials are not in the InputParams class!")


if __name__ == "__main__":
    test_generate_operation_file()
