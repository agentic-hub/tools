# converttofile toolkit
from langchain.tools import BaseTool
from typing import List

def get_converttofile_tools() -> List[BaseTool]:
    """Get all converttofile tools."""
    from . import operations
    return operations.get_tools()

class ConverttofileToolkit:
    """Toolkit for interacting with converttofile."""

    def __init__(self):
        """Initialize the converttofile toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all converttofile tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all converttofile tools with default credentials."""
        return get_converttofile_tools()
