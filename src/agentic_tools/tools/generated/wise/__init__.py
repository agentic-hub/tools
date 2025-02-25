# wise toolkit
from langchain.tools import BaseTool
from typing import List

def get_wise_tools() -> List[BaseTool]:
    """Get all wise tools."""
    from . import operations
    return operations.get_tools()

class WiseToolkit:
    """Toolkit for interacting with wise."""

    def __init__(self):
        """Initialize the wise toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all wise tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all wise tools with default credentials."""
        return get_wise_tools()
