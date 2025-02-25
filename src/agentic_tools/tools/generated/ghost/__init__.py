# ghost toolkit
from langchain.tools import BaseTool
from typing import List

def get_ghost_tools() -> List[BaseTool]:
    """Get all ghost tools."""
    from . import operations
    return operations.get_tools()

class GhostToolkit:
    """Toolkit for interacting with ghost."""

    def __init__(self):
        """Initialize the ghost toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all ghost tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all ghost tools with default credentials."""
        return get_ghost_tools()
