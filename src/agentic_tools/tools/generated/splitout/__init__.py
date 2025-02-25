# splitout toolkit
from langchain.tools import BaseTool
from typing import List

def get_splitout_tools() -> List[BaseTool]:
    """Get all splitout tools."""
    from . import operations
    return operations.get_tools()

class SplitoutToolkit:
    """Toolkit for interacting with splitout."""

    def __init__(self):
        """Initialize the splitout toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all splitout tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all splitout tools with default credentials."""
        return get_splitout_tools()
