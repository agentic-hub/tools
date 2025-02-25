# zammad toolkit
from langchain.tools import BaseTool
from typing import List

def get_zammad_tools() -> List[BaseTool]:
    """Get all zammad tools."""
    from . import operations
    return operations.get_tools()

class ZammadToolkit:
    """Toolkit for interacting with zammad."""

    def __init__(self):
        """Initialize the zammad toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all zammad tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all zammad tools with default credentials."""
        return get_zammad_tools()
