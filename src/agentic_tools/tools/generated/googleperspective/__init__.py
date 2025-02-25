# googleperspective toolkit
from langchain.tools import BaseTool
from typing import List

def get_googleperspective_tools() -> List[BaseTool]:
    """Get all googleperspective tools."""
    from . import operations
    return operations.get_tools()

class GoogleperspectiveToolkit:
    """Toolkit for interacting with googleperspective."""

    def __init__(self):
        """Initialize the googleperspective toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googleperspective tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googleperspective tools with default credentials."""
        return get_googleperspective_tools()
