# awstextract toolkit
from langchain.tools import BaseTool
from typing import List

def get_awstextract_tools() -> List[BaseTool]:
    """Get all awstextract tools."""
    from . import operations
    return operations.get_tools()

class AwsTextractToolkit:
    """Toolkit for interacting with awstextract."""

    def __init__(self):
        """Initialize the awstextract toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all awstextract tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all awstextract tools with default credentials."""
        return get_awstextract_tools()
