# egoi toolkit
from langchain.tools import BaseTool
from typing import List

def get_egoi_tools() -> List[BaseTool]:
    """Get all egoi tools."""
    from . import operations
    return operations.get_tools()

class EgoiToolkit:
    """Toolkit for interacting with egoi."""

    def __init__(self):
        """Initialize the egoi toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all egoi tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all egoi tools with default credentials."""
        return get_egoi_tools()
