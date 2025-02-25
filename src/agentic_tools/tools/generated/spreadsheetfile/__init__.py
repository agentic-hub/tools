# spreadsheetfile toolkit
from langchain.tools import BaseTool
from typing import List

def get_spreadsheetfile_tools() -> List[BaseTool]:
    """Get all spreadsheetfile tools."""
    from . import operations
    return operations.get_tools()

class SpreadsheetfileToolkit:
    """Toolkit for interacting with spreadsheetfile."""

    def __init__(self):
        """Initialize the spreadsheetfile toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all spreadsheetfile tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all spreadsheetfile tools with default credentials."""
        return get_spreadsheetfile_tools()
