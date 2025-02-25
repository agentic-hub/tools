# homeassistant toolkit
from langchain.tools import BaseTool
from typing import List

def get_homeassistant_tools() -> List[BaseTool]:
    """Get all homeassistant tools."""
    from . import operations
    return operations.get_tools()

class HomeassistantToolkit:
    """Toolkit for interacting with homeassistant."""

    def __init__(self):
        """Initialize the homeassistant toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all homeassistant tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all homeassistant tools with default credentials."""
        return get_homeassistant_tools()
