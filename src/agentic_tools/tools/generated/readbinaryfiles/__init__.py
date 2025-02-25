# readbinaryfiles toolkit
from langchain.tools import BaseTool
from typing import List

def get_readbinaryfiles_tools() -> List[BaseTool]:
    """Get all readbinaryfiles tools."""
    from . import operations
    return operations.get_tools()

class ReadbinaryfilesToolkit:
    """Toolkit for interacting with readbinaryfiles."""

    def __init__(self):
        """Initialize the readbinaryfiles toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all readbinaryfiles tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all readbinaryfiles tools with default credentials."""
        return get_readbinaryfiles_tools()
