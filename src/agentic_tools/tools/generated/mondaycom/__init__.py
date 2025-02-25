# mondaycom toolkit
from langchain.tools import BaseTool
from typing import List

def get_mondaycom_tools() -> List[BaseTool]:
    """Get all mondaycom tools."""
    from . import operations
    return operations.get_tools()

class MondaycomToolkit:
    """Toolkit for interacting with mondaycom."""

    def __init__(self):
        """Initialize the mondaycom toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all mondaycom tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all mondaycom tools with default credentials."""
        return get_mondaycom_tools()
