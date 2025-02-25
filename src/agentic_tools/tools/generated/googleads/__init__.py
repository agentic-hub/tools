# googleads toolkit
from langchain.tools import BaseTool
from typing import List

def get_googleads_tools() -> List[BaseTool]:
    """Get all googleads tools."""
    from . import operations
    return operations.get_tools()

class GoogleadsToolkit:
    """Toolkit for interacting with googleads."""

    def __init__(self):
        """Initialize the googleads toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googleads tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googleads tools with default credentials."""
        return get_googleads_tools()
