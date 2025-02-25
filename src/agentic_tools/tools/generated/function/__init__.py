# function toolkit
from langchain.tools import BaseTool
from typing import List

def get_function_tools() -> List[BaseTool]:
    """Get all function tools."""
    from . import operations
    return operations.get_tools()

class FunctionToolkit:
    """Toolkit for interacting with function."""

    def __init__(self):
        """Initialize the function toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all function tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all function tools with default credentials."""
        return get_function_tools()
