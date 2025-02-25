# mocean toolkit
from langchain.tools import BaseTool
from typing import List

def get_mocean_tools() -> List[BaseTool]:
    """Get all mocean tools."""
    from . import operations
    return operations.get_tools()

class MoceanToolkit:
    """Toolkit for interacting with mocean."""

    def __init__(self):
        """Initialize the mocean toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all mocean tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all mocean tools with default credentials."""
        return get_mocean_tools()
