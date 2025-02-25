# linear toolkit
from langchain.tools import BaseTool
from typing import List

def get_linear_tools() -> List[BaseTool]:
    """Get all linear tools."""
    from . import operations
    return operations.get_tools()

class LinearToolkit:
    """Toolkit for interacting with linear."""

    def __init__(self):
        """Initialize the linear toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all linear tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all linear tools with default credentials."""
        return get_linear_tools()
