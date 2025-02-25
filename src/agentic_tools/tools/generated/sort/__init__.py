# sort toolkit
from langchain.tools import BaseTool
from typing import List

def get_sort_tools() -> List[BaseTool]:
    """Get all sort tools."""
    from . import operations
    return operations.get_tools()

class SortToolkit:
    """Toolkit for interacting with sort."""

    def __init__(self):
        """Initialize the sort toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all sort tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all sort tools with default credentials."""
        return get_sort_tools()
