# clockify toolkit
from langchain.tools import BaseTool
from typing import List

def get_clockify_tools() -> List[BaseTool]:
    """Get all clockify tools."""
    from . import operations
    return operations.get_tools()

class ClockifyToolkit:
    """Toolkit for interacting with clockify."""

    def __init__(self):
        """Initialize the clockify toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all clockify tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all clockify tools with default credentials."""
        return get_clockify_tools()
