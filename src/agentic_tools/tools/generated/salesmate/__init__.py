# salesmate toolkit
from langchain.tools import BaseTool
from typing import List

def get_salesmate_tools() -> List[BaseTool]:
    """Get all salesmate tools."""
    from . import operations
    return operations.get_tools()

class SalesmateToolkit:
    """Toolkit for interacting with salesmate."""

    def __init__(self):
        """Initialize the salesmate toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all salesmate tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all salesmate tools with default credentials."""
        return get_salesmate_tools()
