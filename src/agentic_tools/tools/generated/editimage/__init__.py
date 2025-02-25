# editimage toolkit
from langchain.tools import BaseTool
from typing import List

def get_editimage_tools() -> List[BaseTool]:
    """Get all editimage tools."""
    from . import operations
    return operations.get_tools()

class EditimageToolkit:
    """Toolkit for interacting with editimage."""

    def __init__(self):
        """Initialize the editimage toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all editimage tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all editimage tools with default credentials."""
        return get_editimage_tools()
