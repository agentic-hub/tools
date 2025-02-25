# googlefirebaserealtimedatabase toolkit
from langchain.tools import BaseTool
from typing import List

def get_googlefirebaserealtimedatabase_tools() -> List[BaseTool]:
    """Get all googlefirebaserealtimedatabase tools."""
    from . import operations
    return operations.get_tools()

class GooglefirebaserealtimedatabaseToolkit:
    """Toolkit for interacting with googlefirebaserealtimedatabase."""

    def __init__(self):
        """Initialize the googlefirebaserealtimedatabase toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googlefirebaserealtimedatabase tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googlefirebaserealtimedatabase tools with default credentials."""
        return get_googlefirebaserealtimedatabase_tools()
