# cockpit toolkit
from langchain.tools import BaseTool
from typing import List

def get_cockpit_tools() -> List[BaseTool]:
    """Get all cockpit tools."""
    from . import operations
    return operations.get_tools()

class CockpitToolkit:
    """Toolkit for interacting with cockpit."""

    def __init__(self):
        """Initialize the cockpit toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all cockpit tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all cockpit tools with default credentials."""
        return get_cockpit_tools()
