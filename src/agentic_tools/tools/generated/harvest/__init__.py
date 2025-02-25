# harvest toolkit
from langchain.tools import BaseTool
from typing import List

def get_harvest_tools() -> List[BaseTool]:
    """Get all harvest tools."""
    from . import operations
    return operations.get_tools()

class HarvestToolkit:
    """Toolkit for interacting with harvest."""

    def __init__(self):
        """Initialize the harvest toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all harvest tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all harvest tools with default credentials."""
        return get_harvest_tools()
