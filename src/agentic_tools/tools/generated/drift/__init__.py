# drift toolkit
from langchain.tools import BaseTool
from typing import List

def get_drift_tools() -> List[BaseTool]:
    """Get all drift tools."""
    from . import operations
    return operations.get_tools()

class DriftToolkit:
    """Toolkit for interacting with drift."""

    def __init__(self):
        """Initialize the drift toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all drift tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all drift tools with default credentials."""
        return get_drift_tools()
