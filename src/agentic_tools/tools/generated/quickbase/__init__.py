# quickbase toolkit
from langchain.tools import BaseTool
from typing import List

def get_quickbase_tools() -> List[BaseTool]:
    """Get all quickbase tools."""
    from . import operations
    return operations.get_tools()

class QuickbaseToolkit:
    """Toolkit for interacting with quickbase."""

    def __init__(self):
        """Initialize the quickbase toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all quickbase tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all quickbase tools with default credentials."""
        return get_quickbase_tools()
