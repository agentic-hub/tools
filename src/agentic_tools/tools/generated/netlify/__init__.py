# netlify toolkit
from langchain.tools import BaseTool
from typing import List

def get_netlify_tools() -> List[BaseTool]:
    """Get all netlify tools."""
    from . import operations
    return operations.get_tools()

class NetlifyToolkit:
    """Toolkit for interacting with netlify."""

    def __init__(self):
        """Initialize the netlify toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all netlify tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all netlify tools with default credentials."""
        return get_netlify_tools()
