# readwritefile toolkit
from langchain.tools import BaseTool
from typing import List

def get_readwritefile_tools() -> List[BaseTool]:
    """Get all readwritefile tools."""
    from . import operations
    return operations.get_tools()

class ReadwritefileToolkit:
    """Toolkit for interacting with readwritefile."""

    def __init__(self):
        """Initialize the readwritefile toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all readwritefile tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all readwritefile tools with default credentials."""
        return get_readwritefile_tools()
