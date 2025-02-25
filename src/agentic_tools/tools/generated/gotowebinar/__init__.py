# gotowebinar toolkit
from langchain.tools import BaseTool
from typing import List

def get_gotowebinar_tools() -> List[BaseTool]:
    """Get all gotowebinar tools."""
    from . import operations
    return operations.get_tools()

class GotowebinarToolkit:
    """Toolkit for interacting with gotowebinar."""

    def __init__(self):
        """Initialize the gotowebinar toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all gotowebinar tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all gotowebinar tools with default credentials."""
        return get_gotowebinar_tools()
