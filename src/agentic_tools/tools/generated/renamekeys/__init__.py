# renamekeys toolkit
from langchain.tools import BaseTool
from typing import List

def get_renamekeys_tools() -> List[BaseTool]:
    """Get all renamekeys tools."""
    from . import operations
    return operations.get_tools()

class RenamekeysToolkit:
    """Toolkit for interacting with renamekeys."""

    def __init__(self):
        """Initialize the renamekeys toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all renamekeys tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all renamekeys tools with default credentials."""
        return get_renamekeys_tools()
