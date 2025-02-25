# kitemaker toolkit
from langchain.tools import BaseTool
from typing import List

def get_kitemaker_tools() -> List[BaseTool]:
    """Get all kitemaker tools."""
    from . import operations
    return operations.get_tools()

class KitemakerToolkit:
    """Toolkit for interacting with kitemaker."""

    def __init__(self):
        """Initialize the kitemaker toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all kitemaker tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all kitemaker tools with default credentials."""
        return get_kitemaker_tools()
