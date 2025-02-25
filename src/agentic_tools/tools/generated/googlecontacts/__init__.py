# googlecontacts toolkit
from langchain.tools import BaseTool
from typing import List

def get_googlecontacts_tools() -> List[BaseTool]:
    """Get all googlecontacts tools."""
    from . import operations
    return operations.get_tools()

class GooglecontactsToolkit:
    """Toolkit for interacting with googlecontacts."""

    def __init__(self):
        """Initialize the googlecontacts toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googlecontacts tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googlecontacts tools with default credentials."""
        return get_googlecontacts_tools()
