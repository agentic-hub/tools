# bubble toolkit
from langchain.tools import BaseTool
from typing import List

def get_bubble_tools() -> List[BaseTool]:
    """Get all bubble tools."""
    from . import operations
    return operations.get_tools()

class BubbleToolkit:
    """Toolkit for interacting with bubble."""

    def __init__(self):
        """Initialize the bubble toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all bubble tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all bubble tools with default credentials."""
        return get_bubble_tools()
