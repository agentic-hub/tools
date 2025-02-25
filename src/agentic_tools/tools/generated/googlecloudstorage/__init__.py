# googlecloudstorage toolkit
from langchain.tools import BaseTool
from typing import List

def get_googlecloudstorage_tools() -> List[BaseTool]:
    """Get all googlecloudstorage tools."""
    from . import operations
    return operations.get_tools()

class GooglecloudstorageToolkit:
    """Toolkit for interacting with googlecloudstorage."""

    def __init__(self):
        """Initialize the googlecloudstorage toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googlecloudstorage tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googlecloudstorage tools with default credentials."""
        return get_googlecloudstorage_tools()
