# yourls toolkit
from langchain.tools import BaseTool
from typing import List

def get_yourls_tools() -> List[BaseTool]:
    """Get all yourls tools."""
    from . import operations
    return operations.get_tools()

class YourlsToolkit:
    """Toolkit for interacting with yourls."""

    def __init__(self):
        """Initialize the yourls toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all yourls tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all yourls tools with default credentials."""
        return get_yourls_tools()
