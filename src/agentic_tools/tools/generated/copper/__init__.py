# copper toolkit
from langchain.tools import BaseTool
from typing import List

def get_copper_tools() -> List[BaseTool]:
    """Get all copper tools."""
    from . import operations
    return operations.get_tools()

class CopperToolkit:
    """Toolkit for interacting with copper."""

    def __init__(self):
        """Initialize the copper toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all copper tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all copper tools with default credentials."""
        return get_copper_tools()
