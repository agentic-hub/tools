# freshdesk toolkit
from langchain.tools import BaseTool
from typing import List

def get_freshdesk_tools() -> List[BaseTool]:
    """Get all freshdesk tools."""
    from . import operations
    return operations.get_tools()

class FreshdeskToolkit:
    """Toolkit for interacting with freshdesk."""

    def __init__(self):
        """Initialize the freshdesk toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all freshdesk tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all freshdesk tools with default credentials."""
        return get_freshdesk_tools()
