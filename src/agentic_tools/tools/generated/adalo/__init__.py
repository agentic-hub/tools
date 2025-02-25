# adalo toolkit
from langchain.tools import BaseTool
from typing import List

def get_adalo_tools() -> List[BaseTool]:
    """Get all adalo tools."""
    from . import operations
    return operations.get_tools()

class AdaloToolkit:
    """Toolkit for interacting with adalo."""

    def __init__(self):
        """Initialize the adalo toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all adalo tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all adalo tools with default credentials."""
        return get_adalo_tools()
