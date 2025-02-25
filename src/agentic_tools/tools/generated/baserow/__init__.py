# baserow toolkit
from langchain.tools import BaseTool
from typing import List

def get_baserow_tools() -> List[BaseTool]:
    """Get all baserow tools."""
    from . import operations
    return operations.get_tools()

class BaserowToolkit:
    """Toolkit for interacting with baserow."""

    def __init__(self):
        """Initialize the baserow toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all baserow tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all baserow tools with default credentials."""
        return get_baserow_tools()
