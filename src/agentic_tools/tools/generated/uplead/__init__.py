# uplead toolkit
from langchain.tools import BaseTool
from typing import List

def get_uplead_tools() -> List[BaseTool]:
    """Get all uplead tools."""
    from . import operations
    return operations.get_tools()

class UpleadToolkit:
    """Toolkit for interacting with uplead."""

    def __init__(self):
        """Initialize the uplead toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all uplead tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all uplead tools with default credentials."""
        return get_uplead_tools()
