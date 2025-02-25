# dropcontact toolkit
from langchain.tools import BaseTool
from typing import List

def get_dropcontact_tools() -> List[BaseTool]:
    """Get all dropcontact tools."""
    from . import operations
    return operations.get_tools()

class DropcontactToolkit:
    """Toolkit for interacting with dropcontact."""

    def __init__(self):
        """Initialize the dropcontact toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all dropcontact tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all dropcontact tools with default credentials."""
        return get_dropcontact_tools()
