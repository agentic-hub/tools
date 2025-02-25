# googledrive toolkit
from langchain.tools import BaseTool
from typing import List

def get_googledrive_tools() -> List[BaseTool]:
    """Get all googledrive tools."""
    from . import operations
    return operations.get_tools()

class GoogledriveToolkit:
    """Toolkit for interacting with googledrive."""

    def __init__(self):
        """Initialize the googledrive toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googledrive tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googledrive tools with default credentials."""
        return get_googledrive_tools()
