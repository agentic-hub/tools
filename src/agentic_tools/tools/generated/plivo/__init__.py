# plivo toolkit
from langchain.tools import BaseTool
from typing import List

def get_plivo_tools() -> List[BaseTool]:
    """Get all plivo tools."""
    from . import operations
    return operations.get_tools()

class PlivoToolkit:
    """Toolkit for interacting with plivo."""

    def __init__(self):
        """Initialize the plivo toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all plivo tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all plivo tools with default credentials."""
        return get_plivo_tools()
