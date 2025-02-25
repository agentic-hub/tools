# compression toolkit
from langchain.tools import BaseTool
from typing import List

def get_compression_tools() -> List[BaseTool]:
    """Get all compression tools."""
    from . import operations
    return operations.get_tools()

class CompressionToolkit:
    """Toolkit for interacting with compression."""

    def __init__(self):
        """Initialize the compression toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all compression tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all compression tools with default credentials."""
        return get_compression_tools()
