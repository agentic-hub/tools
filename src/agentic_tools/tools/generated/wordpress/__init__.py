# wordpress toolkit
from langchain.tools import BaseTool
from typing import List

def get_wordpress_tools() -> List[BaseTool]:
    """Get all wordpress tools."""
    from . import operations
    return operations.get_tools()

class WordpressToolkit:
    """Toolkit for interacting with wordpress."""

    def __init__(self):
        """Initialize the wordpress toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all wordpress tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all wordpress tools with default credentials."""
        return get_wordpress_tools()
