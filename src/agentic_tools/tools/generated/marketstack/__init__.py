# marketstack toolkit
from langchain.tools import BaseTool
from typing import List

def get_marketstack_tools() -> List[BaseTool]:
    """Get all marketstack tools."""
    from . import operations
    return operations.get_tools()

class MarketstackToolkit:
    """Toolkit for interacting with marketstack."""

    def __init__(self):
        """Initialize the marketstack toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all marketstack tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all marketstack tools with default credentials."""
        return get_marketstack_tools()
