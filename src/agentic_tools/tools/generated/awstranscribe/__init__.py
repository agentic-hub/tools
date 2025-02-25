# awstranscribe toolkit
from langchain.tools import BaseTool
from typing import List

def get_awstranscribe_tools() -> List[BaseTool]:
    """Get all awstranscribe tools."""
    from . import operations
    return operations.get_tools()

class AwsTranscribeToolkit:
    """Toolkit for interacting with awstranscribe."""

    def __init__(self):
        """Initialize the awstranscribe toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all awstranscribe tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all awstranscribe tools with default credentials."""
        return get_awstranscribe_tools()
