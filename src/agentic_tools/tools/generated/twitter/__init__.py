# twitter toolkit
from langchain.tools import BaseTool
from typing import List

def get_twitter_tools() -> List[BaseTool]:
    """Get all twitter tools."""
    from . import operations
    return operations.get_tools()

class TwitterToolkit:
    """Toolkit for interacting with twitter."""

    def __init__(self):
        """Initialize the twitter toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all twitter tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all twitter tools with default credentials."""
        return get_twitter_tools()
