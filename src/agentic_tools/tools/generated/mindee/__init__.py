# mindee toolkit
from langchain.tools import BaseTool
from typing import List

def get_mindee_tools() -> List[BaseTool]:
    """Get all mindee tools."""
    from . import operations
    return operations.get_tools()

class MindeeToolkit:
    """Toolkit for interacting with mindee."""

    def __init__(self):
        """Initialize the mindee toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all mindee tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all mindee tools with default credentials."""
        return get_mindee_tools()
