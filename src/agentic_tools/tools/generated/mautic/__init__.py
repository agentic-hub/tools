# mautic toolkit
from langchain.tools import BaseTool
from typing import List

def get_mautic_tools() -> List[BaseTool]:
    """Get all mautic tools."""
    from . import operations
    return operations.get_tools()

class MauticToolkit:
    """Toolkit for interacting with mautic."""

    def __init__(self):
        """Initialize the mautic toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all mautic tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all mautic tools with default credentials."""
        return get_mautic_tools()
