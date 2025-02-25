# readpdf toolkit
from langchain.tools import BaseTool
from typing import List

def get_readpdf_tools() -> List[BaseTool]:
    """Get all readpdf tools."""
    from . import operations
    return operations.get_tools()

class ReadpdfToolkit:
    """Toolkit for interacting with readpdf."""

    def __init__(self):
        """Initialize the readpdf toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all readpdf tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all readpdf tools with default credentials."""
        return get_readpdf_tools()
