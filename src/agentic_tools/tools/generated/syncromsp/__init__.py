# syncromsp toolkit
from langchain.tools import BaseTool
from typing import List

def get_syncromsp_tools() -> List[BaseTool]:
    """Get all syncromsp tools."""
    from . import operations
    return operations.get_tools()

class SyncromspToolkit:
    """Toolkit for interacting with syncromsp."""

    def __init__(self):
        """Initialize the syncromsp toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all syncromsp tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all syncromsp tools with default credentials."""
        return get_syncromsp_tools()
