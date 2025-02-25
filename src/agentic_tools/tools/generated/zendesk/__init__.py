# zendesk toolkit
from langchain.tools import BaseTool
from typing import List

def get_zendesk_tools() -> List[BaseTool]:
    """Get all zendesk tools."""
    from . import operations
    return operations.get_tools()

class ZendeskToolkit:
    """Toolkit for interacting with zendesk."""

    def __init__(self):
        """Initialize the zendesk toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all zendesk tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all zendesk tools with default credentials."""
        return get_zendesk_tools()
