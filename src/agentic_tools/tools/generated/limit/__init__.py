# limit toolkit
from langchain.tools import BaseTool
from typing import List

def get_limit_tools() -> List[BaseTool]:
    """Get all limit tools."""
    from . import operations
    return operations.get_tools()

class LimitToolkit:
    """Toolkit for interacting with limit."""

    def __init__(self):
        """Initialize the limit toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all limit tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all limit tools with default credentials."""
        return get_limit_tools()
