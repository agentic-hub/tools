# twist toolkit
from langchain.tools import BaseTool
from typing import List

def get_twist_tools() -> List[BaseTool]:
    """Get all twist tools."""
    from . import operations
    return operations.get_tools()

class TwistToolkit:
    """Toolkit for interacting with twist."""

    def __init__(self):
        """Initialize the twist toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all twist tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all twist tools with default credentials."""
        return get_twist_tools()
