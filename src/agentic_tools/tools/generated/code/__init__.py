# code toolkit
from langchain.tools import BaseTool
from typing import List

def get_code_tools() -> List[BaseTool]:
    """Get all code tools."""
    from . import operations
    return operations.get_tools()

class CodeToolkit:
    """Toolkit for interacting with code."""

    def __init__(self):
        """Initialize the code toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all code tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all code tools with default credentials."""
        return get_code_tools()
