# interval toolkit
from langchain.tools import BaseTool
from typing import List

def get_interval_tools() -> List[BaseTool]:
    """Get all interval tools."""
    from . import operations
    return operations.get_tools()

class IntervalToolkit:
    """Toolkit for interacting with interval."""

    def __init__(self):
        """Initialize the interval toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all interval tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all interval tools with default credentials."""
        return get_interval_tools()
