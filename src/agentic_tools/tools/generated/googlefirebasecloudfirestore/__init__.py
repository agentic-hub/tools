# googlefirebasecloudfirestore toolkit
from langchain.tools import BaseTool
from typing import List

def get_googlefirebasecloudfirestore_tools() -> List[BaseTool]:
    """Get all googlefirebasecloudfirestore tools."""
    from . import operations
    return operations.get_tools()

class GooglefirebasecloudfirestoreToolkit:
    """Toolkit for interacting with googlefirebasecloudfirestore."""

    def __init__(self):
        """Initialize the googlefirebasecloudfirestore toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googlefirebasecloudfirestore tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googlefirebasecloudfirestore tools with default credentials."""
        return get_googlefirebasecloudfirestore_tools()
