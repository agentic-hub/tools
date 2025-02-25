# filemaker toolkit
from langchain.tools import BaseTool
from typing import List

def get_filemaker_tools() -> List[BaseTool]:
    """Get all filemaker tools."""
    from . import operations
    return operations.get_tools()

class FilemakerToolkit:
    """Toolkit for interacting with filemaker."""

    def __init__(self):
        """Initialize the filemaker toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all filemaker tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all filemaker tools with default credentials."""
        return get_filemaker_tools()
