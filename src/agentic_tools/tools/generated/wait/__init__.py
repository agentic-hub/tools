# wait toolkit
from langchain.tools import BaseTool
from typing import List

def get_wait_tools() -> List[BaseTool]:
    """Get all wait tools."""
    from . import operations
    return operations.get_tools()

class WaitToolkit:
    """Toolkit for interacting with wait."""

    def __init__(self):
        """Initialize the wait toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all wait tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all wait tools with default credentials."""
        return get_wait_tools()
