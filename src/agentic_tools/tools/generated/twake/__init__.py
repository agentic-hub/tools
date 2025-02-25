# twake toolkit
from langchain.tools import BaseTool
from typing import List

def get_twake_tools() -> List[BaseTool]:
    """Get all twake tools."""
    from . import operations
    return operations.get_tools()

class TwakeToolkit:
    """Toolkit for interacting with twake."""

    def __init__(self):
        """Initialize the twake toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all twake tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all twake tools with default credentials."""
        return get_twake_tools()
