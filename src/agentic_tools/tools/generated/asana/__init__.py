# asana toolkit
from langchain.tools import BaseTool
from typing import List

def get_asana_tools() -> List[BaseTool]:
    """Get all asana tools."""
    from . import operations
    return operations.get_tools()

class AsanaToolkit:
    """Toolkit for interacting with asana."""

    def __init__(self):
        """Initialize the asana toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all asana tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all asana tools with default credentials."""
        return get_asana_tools()
