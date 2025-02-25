# readbinaryfile toolkit
from langchain.tools import BaseTool
from typing import List

def get_readbinaryfile_tools() -> List[BaseTool]:
    """Get all readbinaryfile tools."""
    from . import operations
    return operations.get_tools()

class ReadbinaryfileToolkit:
    """Toolkit for interacting with readbinaryfile."""

    def __init__(self):
        """Initialize the readbinaryfile toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all readbinaryfile tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all readbinaryfile tools with default credentials."""
        return get_readbinaryfile_tools()
