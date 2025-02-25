# vero toolkit
from langchain.tools import BaseTool
from typing import List

def get_vero_tools() -> List[BaseTool]:
    """Get all vero tools."""
    from . import operations
    return operations.get_tools()

class VeroToolkit:
    """Toolkit for interacting with vero."""

    def __init__(self):
        """Initialize the vero toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all vero tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all vero tools with default credentials."""
        return get_vero_tools()
