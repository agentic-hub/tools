# gotify toolkit
from langchain.tools import BaseTool
from typing import List

def get_gotify_tools() -> List[BaseTool]:
    """Get all gotify tools."""
    from . import operations
    return operations.get_tools()

class GotifyToolkit:
    """Toolkit for interacting with gotify."""

    def __init__(self):
        """Initialize the gotify toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all gotify tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all gotify tools with default credentials."""
        return get_gotify_tools()
