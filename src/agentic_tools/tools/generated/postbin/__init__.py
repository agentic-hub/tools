# postbin toolkit
from langchain.tools import BaseTool
from typing import List

def get_postbin_tools() -> List[BaseTool]:
    """Get all postbin tools."""
    from . import operations
    return operations.get_tools()

class PostbinToolkit:
    """Toolkit for interacting with postbin."""

    def __init__(self):
        """Initialize the postbin toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all postbin tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all postbin tools with default credentials."""
        return get_postbin_tools()
