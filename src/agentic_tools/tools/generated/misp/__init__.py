# misp toolkit
from langchain.tools import BaseTool
from typing import List

def get_misp_tools() -> List[BaseTool]:
    """Get all misp tools."""
    from . import operations
    return operations.get_tools()

class MispToolkit:
    """Toolkit for interacting with misp."""

    def __init__(self):
        """Initialize the misp toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all misp tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all misp tools with default credentials."""
        return get_misp_tools()
