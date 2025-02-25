# pushover toolkit
from langchain.tools import BaseTool
from typing import List

def get_pushover_tools() -> List[BaseTool]:
    """Get all pushover tools."""
    from . import operations
    return operations.get_tools()

class PushoverToolkit:
    """Toolkit for interacting with pushover."""

    def __init__(self):
        """Initialize the pushover toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all pushover tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all pushover tools with default credentials."""
        return get_pushover_tools()
