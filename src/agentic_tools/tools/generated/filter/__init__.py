# filter toolkit
from langchain.tools import BaseTool
from typing import List

def get_filter_tools() -> List[BaseTool]:
    """Get all filter tools."""
    from . import operations
    return operations.get_tools()

class FilterToolkit:
    """Toolkit for interacting with filter."""

    def __init__(self):
        """Initialize the filter toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all filter tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all filter tools with default credentials."""
        return get_filter_tools()
