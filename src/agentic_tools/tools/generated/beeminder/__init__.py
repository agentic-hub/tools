# beeminder toolkit
from langchain.tools import BaseTool
from typing import List

def get_beeminder_tools() -> List[BaseTool]:
    """Get all beeminder tools."""
    from . import operations
    return operations.get_tools()

class BeeminderToolkit:
    """Toolkit for interacting with beeminder."""

    def __init__(self):
        """Initialize the beeminder toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all beeminder tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all beeminder tools with default credentials."""
        return get_beeminder_tools()
