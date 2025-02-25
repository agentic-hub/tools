# hubspot toolkit
from langchain.tools import BaseTool
from typing import List

def get_hubspot_tools() -> List[BaseTool]:
    """Get all hubspot tools."""
    from . import operations
    return operations.get_tools()

class HubspotToolkit:
    """Toolkit for interacting with hubspot."""

    def __init__(self):
        """Initialize the hubspot toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all hubspot tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all hubspot tools with default credentials."""
        return get_hubspot_tools()
