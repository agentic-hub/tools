# removeduplicates toolkit
from langchain.tools import BaseTool
from typing import List

def get_removeduplicates_tools() -> List[BaseTool]:
    """Get all removeduplicates tools."""
    from . import operations
    return operations.get_tools()

class RemoveduplicatesToolkit:
    """Toolkit for interacting with removeduplicates."""

    def __init__(self):
        """Initialize the removeduplicates toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all removeduplicates tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all removeduplicates tools with default credentials."""
        return get_removeduplicates_tools()
