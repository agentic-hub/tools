# markdown toolkit
from langchain.tools import BaseTool
from typing import List

def get_markdown_tools() -> List[BaseTool]:
    """Get all markdown tools."""
    from . import operations
    return operations.get_tools()

class MarkdownToolkit:
    """Toolkit for interacting with markdown."""

    def __init__(self):
        """Initialize the markdown toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all markdown tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all markdown tools with default credentials."""
        return get_markdown_tools()
