# contentful toolkit
from langchain.tools import BaseTool
from typing import List

def get_contentful_tools() -> List[BaseTool]:
    """Get all contentful tools."""
    from . import operations
    return operations.get_tools()

class ContentfulToolkit:
    """Toolkit for interacting with contentful."""

    def __init__(self):
        """Initialize the contentful toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all contentful tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all contentful tools with default credentials."""
        return get_contentful_tools()
