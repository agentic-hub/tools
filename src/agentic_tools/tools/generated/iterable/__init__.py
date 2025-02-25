# iterable toolkit
from langchain.tools import BaseTool
from typing import List

def get_iterable_tools() -> List[BaseTool]:
    """Get all iterable tools."""
    from . import operations
    return operations.get_tools()

class IterableToolkit:
    """Toolkit for interacting with iterable."""

    def __init__(self):
        """Initialize the iterable toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all iterable tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all iterable tools with default credentials."""
        return get_iterable_tools()
