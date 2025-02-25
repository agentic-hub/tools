# set toolkit
from langchain.tools import BaseTool
from typing import List

def get_set_tools() -> List[BaseTool]:
    """Get all set tools."""
    from . import operations
    return operations.get_tools()

class SetToolkit:
    """Toolkit for interacting with set."""

    def __init__(self):
        """Initialize the set toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all set tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all set tools with default credentials."""
        return get_set_tools()
