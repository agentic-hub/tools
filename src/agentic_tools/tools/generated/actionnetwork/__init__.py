# actionnetwork toolkit
from langchain.tools import BaseTool
from typing import List

def get_actionnetwork_tools() -> List[BaseTool]:
    """Get all actionnetwork tools."""
    from . import operations
    return operations.get_tools()

class ActionnetworkToolkit:
    """Toolkit for interacting with actionnetwork."""

    def __init__(self):
        """Initialize the actionnetwork toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all actionnetwork tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all actionnetwork tools with default credentials."""
        return get_actionnetwork_tools()
