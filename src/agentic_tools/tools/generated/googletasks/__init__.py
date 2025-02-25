# googletasks toolkit
from langchain.tools import BaseTool
from typing import List

def get_googletasks_tools() -> List[BaseTool]:
    """Get all googletasks tools."""
    from . import operations
    return operations.get_tools()

class GoogletasksToolkit:
    """Toolkit for interacting with googletasks."""

    def __init__(self):
        """Initialize the googletasks toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googletasks tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googletasks tools with default credentials."""
        return get_googletasks_tools()
