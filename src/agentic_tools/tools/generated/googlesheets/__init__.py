# googlesheets toolkit
from langchain.tools import BaseTool
from typing import List

def get_googlesheets_tools() -> List[BaseTool]:
    """Get all googlesheets tools."""
    from . import operations
    return operations.get_tools()

class GooglesheetsToolkit:
    """Toolkit for interacting with googlesheets."""

    def __init__(self):
        """Initialize the googlesheets toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googlesheets tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googlesheets tools with default credentials."""
        return get_googlesheets_tools()
