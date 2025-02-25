# keap toolkit
from langchain.tools import BaseTool
from typing import List

def get_keap_tools() -> List[BaseTool]:
    """Get all keap tools."""
    from . import operations
    return operations.get_tools()

class KeapToolkit:
    """Toolkit for interacting with keap."""

    def __init__(self):
        """Initialize the keap toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all keap tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all keap tools with default credentials."""
        return get_keap_tools()
