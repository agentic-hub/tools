# rocketchat toolkit
from langchain.tools import BaseTool
from typing import List

def get_rocketchat_tools() -> List[BaseTool]:
    """Get all rocketchat tools."""
    from . import operations
    return operations.get_tools()

class RocketchatToolkit:
    """Toolkit for interacting with rocketchat."""

    def __init__(self):
        """Initialize the rocketchat toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all rocketchat tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all rocketchat tools with default credentials."""
        return get_rocketchat_tools()
