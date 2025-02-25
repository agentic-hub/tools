# brandfetch toolkit
from langchain.tools import BaseTool
from typing import List

def get_brandfetch_tools() -> List[BaseTool]:
    """Get all brandfetch tools."""
    from . import operations
    return operations.get_tools()

class BrandfetchToolkit:
    """Toolkit for interacting with brandfetch."""

    def __init__(self):
        """Initialize the brandfetch toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all brandfetch tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all brandfetch tools with default credentials."""
        return get_brandfetch_tools()
