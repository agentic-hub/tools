# signl4 toolkit
from langchain.tools import BaseTool
from typing import List

def get_signl4_tools() -> List[BaseTool]:
    """Get all signl4 tools."""
    from . import operations
    return operations.get_tools()

class SignlToolkit:
    """Toolkit for interacting with signl4."""

    def __init__(self):
        """Initialize the signl4 toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all signl4 tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all signl4 tools with default credentials."""
        return get_signl4_tools()
