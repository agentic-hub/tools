# dhl toolkit
from langchain.tools import BaseTool
from typing import List

def get_dhl_tools() -> List[BaseTool]:
    """Get all dhl tools."""
    from . import operations
    return operations.get_tools()

class DhlToolkit:
    """Toolkit for interacting with dhl."""

    def __init__(self):
        """Initialize the dhl toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all dhl tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all dhl tools with default credentials."""
        return get_dhl_tools()
