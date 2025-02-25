# if toolkit
from langchain.tools import BaseTool
from typing import List

def get_if_tools() -> List[BaseTool]:
    """Get all if tools."""
    from . import operations
    return operations.get_tools()

class IfToolkit:
    """Toolkit for interacting with if."""

    def __init__(self):
        """Initialize the if toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all if tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all if tools with default credentials."""
        return get_if_tools()
