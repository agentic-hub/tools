# hunter toolkit
from langchain.tools import BaseTool
from typing import List

def get_hunter_tools() -> List[BaseTool]:
    """Get all hunter tools."""
    from . import operations
    return operations.get_tools()

class HunterToolkit:
    """Toolkit for interacting with hunter."""

    def __init__(self):
        """Initialize the hunter toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all hunter tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all hunter tools with default credentials."""
        return get_hunter_tools()
