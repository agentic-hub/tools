# writebinaryfile toolkit
from langchain.tools import BaseTool
from typing import List

def get_writebinaryfile_tools() -> List[BaseTool]:
    """Get all writebinaryfile tools."""
    from . import operations
    return operations.get_tools()

class WritebinaryfileToolkit:
    """Toolkit for interacting with writebinaryfile."""

    def __init__(self):
        """Initialize the writebinaryfile toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all writebinaryfile tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all writebinaryfile tools with default credentials."""
        return get_writebinaryfile_tools()
