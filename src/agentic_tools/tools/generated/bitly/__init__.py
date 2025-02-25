# bitly toolkit
from langchain.tools import BaseTool
from typing import List

def get_bitly_tools() -> List[BaseTool]:
    """Get all bitly tools."""
    from . import operations
    return operations.get_tools()

class BitlyToolkit:
    """Toolkit for interacting with bitly."""

    def __init__(self):
        """Initialize the bitly toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all bitly tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all bitly tools with default credentials."""
        return get_bitly_tools()
