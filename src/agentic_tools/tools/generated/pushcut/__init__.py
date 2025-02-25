# pushcut toolkit
from langchain.tools import BaseTool
from typing import List

def get_pushcut_tools() -> List[BaseTool]:
    """Get all pushcut tools."""
    from . import operations
    return operations.get_tools()

class PushcutToolkit:
    """Toolkit for interacting with pushcut."""

    def __init__(self):
        """Initialize the pushcut toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all pushcut tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all pushcut tools with default credentials."""
        return get_pushcut_tools()
