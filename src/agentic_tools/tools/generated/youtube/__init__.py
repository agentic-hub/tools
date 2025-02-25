# youtube toolkit
from langchain.tools import BaseTool
from typing import List

def get_youtube_tools() -> List[BaseTool]:
    """Get all youtube tools."""
    from . import operations
    return operations.get_tools()

class YoutubeToolkit:
    """Toolkit for interacting with youtube."""

    def __init__(self):
        """Initialize the youtube toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all youtube tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all youtube tools with default credentials."""
        return get_youtube_tools()
