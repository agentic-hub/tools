# hackernews toolkit
from langchain.tools import BaseTool
from typing import List

def get_hackernews_tools() -> List[BaseTool]:
    """Get all hackernews tools."""
    from . import operations
    return operations.get_tools()

class HackernewsToolkit:
    """Toolkit for interacting with hackernews."""

    def __init__(self):
        """Initialize the hackernews toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all hackernews tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all hackernews tools with default credentials."""
        return get_hackernews_tools()
