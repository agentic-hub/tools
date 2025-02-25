# stickynote toolkit
from langchain.tools import BaseTool
from typing import List

def get_stickynote_tools() -> List[BaseTool]:
    """Get all stickynote tools."""
    from . import operations
    return operations.get_tools()

class StickynoteToolkit:
    """Toolkit for interacting with stickynote."""

    def __init__(self):
        """Initialize the stickynote toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all stickynote tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all stickynote tools with default credentials."""
        return get_stickynote_tools()
