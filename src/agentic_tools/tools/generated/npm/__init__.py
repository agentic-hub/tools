# npm toolkit
from langchain.tools import BaseTool
from typing import List

def get_npm_tools() -> List[BaseTool]:
    """Get all npm tools."""
    from . import operations
    return operations.get_tools()

class NpmToolkit:
    """Toolkit for interacting with npm."""

    def __init__(self):
        """Initialize the npm toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all npm tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all npm tools with default credentials."""
        return get_npm_tools()
