# functionitem toolkit
from langchain.tools import BaseTool
from typing import List

def get_functionitem_tools() -> List[BaseTool]:
    """Get all functionitem tools."""
    from . import operations
    return operations.get_tools()

class FunctionitemToolkit:
    """Toolkit for interacting with functionitem."""

    def __init__(self):
        """Initialize the functionitem toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all functionitem tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all functionitem tools with default credentials."""
        return get_functionitem_tools()
