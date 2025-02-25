# quickbooks toolkit
from langchain.tools import BaseTool
from typing import List

def get_quickbooks_tools() -> List[BaseTool]:
    """Get all quickbooks tools."""
    from . import operations
    return operations.get_tools()

class QuickbooksToolkit:
    """Toolkit for interacting with quickbooks."""

    def __init__(self):
        """Initialize the quickbooks toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all quickbooks tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all quickbooks tools with default credentials."""
        return get_quickbooks_tools()
