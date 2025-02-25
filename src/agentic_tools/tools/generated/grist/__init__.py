# grist toolkit
from langchain.tools import BaseTool
from typing import List

def get_grist_tools() -> List[BaseTool]:
    """Get all grist tools."""
    from . import operations
    return operations.get_tools()

class GristToolkit:
    """Toolkit for interacting with grist."""

    def __init__(self):
        """Initialize the grist toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all grist tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all grist tools with default credentials."""
        return get_grist_tools()
