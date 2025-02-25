# highlevel toolkit
from langchain.tools import BaseTool
from typing import List

def get_highlevel_tools() -> List[BaseTool]:
    """Get all highlevel tools."""
    from . import operations
    return operations.get_tools()

class HighlevelToolkit:
    """Toolkit for interacting with highlevel."""

    def __init__(self):
        """Initialize the highlevel toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all highlevel tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all highlevel tools with default credentials."""
        return get_highlevel_tools()
