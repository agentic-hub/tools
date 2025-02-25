# gsuiteadmin toolkit
from langchain.tools import BaseTool
from typing import List

def get_gsuiteadmin_tools() -> List[BaseTool]:
    """Get all gsuiteadmin tools."""
    from . import operations
    return operations.get_tools()

class GsuiteadminToolkit:
    """Toolkit for interacting with gsuiteadmin."""

    def __init__(self):
        """Initialize the gsuiteadmin toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all gsuiteadmin tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all gsuiteadmin tools with default credentials."""
        return get_gsuiteadmin_tools()
