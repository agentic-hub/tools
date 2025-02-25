# stackby toolkit
from langchain.tools import BaseTool
from typing import List

def get_stackby_tools() -> List[BaseTool]:
    """Get all stackby tools."""
    from . import operations
    return operations.get_tools()

class StackbyToolkit:
    """Toolkit for interacting with stackby."""

    def __init__(self):
        """Initialize the stackby toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all stackby tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all stackby tools with default credentials."""
        return get_stackby_tools()
