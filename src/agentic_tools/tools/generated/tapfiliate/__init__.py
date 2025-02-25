# tapfiliate toolkit
from langchain.tools import BaseTool
from typing import List

def get_tapfiliate_tools() -> List[BaseTool]:
    """Get all tapfiliate tools."""
    from . import operations
    return operations.get_tools()

class TapfiliateToolkit:
    """Toolkit for interacting with tapfiliate."""

    def __init__(self):
        """Initialize the tapfiliate toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all tapfiliate tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all tapfiliate tools with default credentials."""
        return get_tapfiliate_tools()
