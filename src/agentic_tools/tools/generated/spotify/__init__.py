# spotify toolkit
from langchain.tools import BaseTool
from typing import List

def get_spotify_tools() -> List[BaseTool]:
    """Get all spotify tools."""
    from . import operations
    return operations.get_tools()

class SpotifyToolkit:
    """Toolkit for interacting with spotify."""

    def __init__(self):
        """Initialize the spotify toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all spotify tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all spotify tools with default credentials."""
        return get_spotify_tools()
