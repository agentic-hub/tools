# seatable toolkit
from langchain.tools import BaseTool
from typing import List

def get_seatable_tools() -> List[BaseTool]:
    """Get all seatable tools."""
    from . import operations
    return operations.get_tools()

class SeatableToolkit:
    """Toolkit for interacting with seatable."""

    def __init__(self):
        """Initialize the seatable toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all seatable tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all seatable tools with default credentials."""
        return get_seatable_tools()
