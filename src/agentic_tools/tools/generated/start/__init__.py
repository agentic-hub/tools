# start toolkit
from langchain.tools import BaseTool
from typing import List

def get_start_tools() -> List[BaseTool]:
    """Get all start tools."""
    from . import operations
    return operations.get_tools()

class StartToolkit:
    """Toolkit for interacting with start."""

    def __init__(self):
        """Initialize the start toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all start tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all start tools with default credentials."""
        return get_start_tools()
