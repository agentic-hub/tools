# freshworkscrm toolkit
from langchain.tools import BaseTool
from typing import List

def get_freshworkscrm_tools() -> List[BaseTool]:
    """Get all freshworkscrm tools."""
    from . import operations
    return operations.get_tools()

class FreshworkscrmToolkit:
    """Toolkit for interacting with freshworkscrm."""

    def __init__(self):
        """Initialize the freshworkscrm toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all freshworkscrm tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all freshworkscrm tools with default credentials."""
        return get_freshworkscrm_tools()
