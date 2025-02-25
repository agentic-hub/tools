# peekalink toolkit
from langchain.tools import BaseTool
from typing import List

def get_peekalink_tools() -> List[BaseTool]:
    """Get all peekalink tools."""
    from . import operations
    return operations.get_tools()

class PeekalinkToolkit:
    """Toolkit for interacting with peekalink."""

    def __init__(self):
        """Initialize the peekalink toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all peekalink tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all peekalink tools with default credentials."""
        return get_peekalink_tools()
