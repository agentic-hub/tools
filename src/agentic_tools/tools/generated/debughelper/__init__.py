# debughelper toolkit
from langchain.tools import BaseTool
from typing import List

def get_debughelper_tools() -> List[BaseTool]:
    """Get all debughelper tools."""
    from . import operations
    return operations.get_tools()

class DebughelperToolkit:
    """Toolkit for interacting with debughelper."""

    def __init__(self):
        """Initialize the debughelper toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all debughelper tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all debughelper tools with default credentials."""
        return get_debughelper_tools()
