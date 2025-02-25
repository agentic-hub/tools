# vonage toolkit
from langchain.tools import BaseTool
from typing import List

def get_vonage_tools() -> List[BaseTool]:
    """Get all vonage tools."""
    from . import operations
    return operations.get_tools()

class VonageToolkit:
    """Toolkit for interacting with vonage."""

    def __init__(self):
        """Initialize the vonage toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all vonage tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all vonage tools with default credentials."""
        return get_vonage_tools()
