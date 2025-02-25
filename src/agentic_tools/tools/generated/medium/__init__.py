# medium toolkit
from langchain.tools import BaseTool
from typing import List

def get_medium_tools() -> List[BaseTool]:
    """Get all medium tools."""
    from . import operations
    return operations.get_tools()

class MediumToolkit:
    """Toolkit for interacting with medium."""

    def __init__(self):
        """Initialize the medium toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all medium tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all medium tools with default credentials."""
        return get_medium_tools()
