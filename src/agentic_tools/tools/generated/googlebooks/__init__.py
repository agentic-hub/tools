# googlebooks toolkit
from langchain.tools import BaseTool
from typing import List

def get_googlebooks_tools() -> List[BaseTool]:
    """Get all googlebooks tools."""
    from . import operations
    return operations.get_tools()

class GooglebooksToolkit:
    """Toolkit for interacting with googlebooks."""

    def __init__(self):
        """Initialize the googlebooks toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googlebooks tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googlebooks tools with default credentials."""
        return get_googlebooks_tools()
