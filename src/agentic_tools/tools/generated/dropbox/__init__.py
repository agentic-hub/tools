# dropbox toolkit
from langchain.tools import BaseTool
from typing import List

def get_dropbox_tools() -> List[BaseTool]:
    """Get all dropbox tools."""
    from . import operations
    return operations.get_tools()

class DropboxToolkit:
    """Toolkit for interacting with dropbox."""

    def __init__(self):
        """Initialize the dropbox toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all dropbox tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all dropbox tools with default credentials."""
        return get_dropbox_tools()
