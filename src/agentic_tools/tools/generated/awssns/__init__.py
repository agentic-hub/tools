# awssns toolkit
from langchain.tools import BaseTool
from typing import List

def get_awssns_tools() -> List[BaseTool]:
    """Get all awssns tools."""
    from . import operations
    return operations.get_tools()

class AwsSnsToolkit:
    """Toolkit for interacting with awssns."""

    def __init__(self):
        """Initialize the awssns toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all awssns tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all awssns tools with default credentials."""
        return get_awssns_tools()
