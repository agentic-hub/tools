# stopanderror toolkit
from langchain.tools import BaseTool
from typing import List

def get_stopanderror_tools() -> List[BaseTool]:
    """Get all stopanderror tools."""
    from . import operations
    return operations.get_tools()

class StopanderrorToolkit:
    """Toolkit for interacting with stopanderror."""

    def __init__(self):
        """Initialize the stopanderror toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all stopanderror tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all stopanderror tools with default credentials."""
        return get_stopanderror_tools()
