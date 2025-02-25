# zoom toolkit
from langchain.tools import BaseTool
from typing import List

def get_zoom_tools() -> List[BaseTool]:
    """Get all zoom tools."""
    from . import operations
    return operations.get_tools()

class ZoomToolkit:
    """Toolkit for interacting with zoom."""

    def __init__(self):
        """Initialize the zoom toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all zoom tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all zoom tools with default credentials."""
        return get_zoom_tools()
