# googledocs toolkit
from langchain.tools import BaseTool
from typing import List

def get_googledocs_tools() -> List[BaseTool]:
    """Get all googledocs tools."""
    from . import operations
    return operations.get_tools()

class GoogledocsToolkit:
    """Toolkit for interacting with googledocs."""

    def __init__(self):
        """Initialize the googledocs toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googledocs tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googledocs tools with default credentials."""
        return get_googledocs_tools()
