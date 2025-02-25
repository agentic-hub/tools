# raindrop toolkit
from langchain.tools import BaseTool
from typing import List

def get_raindrop_tools() -> List[BaseTool]:
    """Get all raindrop tools."""
    from . import operations
    return operations.get_tools()

class RaindropToolkit:
    """Toolkit for interacting with raindrop."""

    def __init__(self):
        """Initialize the raindrop toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all raindrop tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all raindrop tools with default credentials."""
        return get_raindrop_tools()
