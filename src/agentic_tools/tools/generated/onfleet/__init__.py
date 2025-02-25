# onfleet toolkit
from langchain.tools import BaseTool
from typing import List

def get_onfleet_tools() -> List[BaseTool]:
    """Get all onfleet tools."""
    from . import operations
    return operations.get_tools()

class OnfleetToolkit:
    """Toolkit for interacting with onfleet."""

    def __init__(self):
        """Initialize the onfleet toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all onfleet tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all onfleet tools with default credentials."""
        return get_onfleet_tools()
