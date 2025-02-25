# notion toolkit
from langchain.tools import BaseTool
from typing import List

def get_notion_tools() -> List[BaseTool]:
    """Get all notion tools."""
    from . import operations
    return operations.get_tools()

class NotionToolkit:
    """Toolkit for interacting with notion."""

    def __init__(self):
        """Initialize the notion toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all notion tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all notion tools with default credentials."""
        return get_notion_tools()
