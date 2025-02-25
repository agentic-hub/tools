# chargebee toolkit
from langchain.tools import BaseTool
from typing import List

def get_chargebee_tools() -> List[BaseTool]:
    """Get all chargebee tools."""
    from . import operations
    return operations.get_tools()

class ChargebeeToolkit:
    """Toolkit for interacting with chargebee."""

    def __init__(self):
        """Initialize the chargebee toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all chargebee tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all chargebee tools with default credentials."""
        return get_chargebee_tools()
