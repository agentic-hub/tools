# helpscout toolkit
from langchain.tools import BaseTool
from typing import List

def get_helpscout_tools() -> List[BaseTool]:
    """Get all helpscout tools."""
    from . import operations
    return operations.get_tools()

class HelpscoutToolkit:
    """Toolkit for interacting with helpscout."""

    def __init__(self):
        """Initialize the helpscout toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all helpscout tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all helpscout tools with default credentials."""
        return get_helpscout_tools()
