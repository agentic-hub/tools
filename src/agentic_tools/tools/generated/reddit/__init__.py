# reddit toolkit
from langchain.tools import BaseTool
from typing import List

def get_reddit_tools() -> List[BaseTool]:
    """Get all reddit tools."""
    from . import operations
    return operations.get_tools()

class RedditToolkit:
    """Toolkit for interacting with reddit."""

    def __init__(self):
        """Initialize the reddit toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all reddit tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all reddit tools with default credentials."""
        return get_reddit_tools()
