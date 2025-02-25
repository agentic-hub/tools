# itemlists toolkit
from langchain.tools import BaseTool
from typing import List

def get_itemlists_tools() -> List[BaseTool]:
    """Get all itemlists tools."""
    from . import operations
    return operations.get_tools()

class ItemlistsToolkit:
    """Toolkit for interacting with itemlists."""

    def __init__(self):
        """Initialize the itemlists toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all itemlists tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all itemlists tools with default credentials."""
        return get_itemlists_tools()
