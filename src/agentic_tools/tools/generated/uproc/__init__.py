# uproc toolkit
from langchain.tools import BaseTool
from typing import List

def get_uproc_tools() -> List[BaseTool]:
    """Get all uproc tools."""
    from . import operations
    return operations.get_tools()

class UprocToolkit:
    """Toolkit for interacting with uproc."""

    def __init__(self):
        """Initialize the uproc toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all uproc tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all uproc tools with default credentials."""
        return get_uproc_tools()
