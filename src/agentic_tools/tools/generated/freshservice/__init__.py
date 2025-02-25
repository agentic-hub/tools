# freshservice toolkit
from langchain.tools import BaseTool
from typing import List

def get_freshservice_tools() -> List[BaseTool]:
    """Get all freshservice tools."""
    from . import operations
    return operations.get_tools()

class FreshserviceToolkit:
    """Toolkit for interacting with freshservice."""

    def __init__(self):
        """Initialize the freshservice toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all freshservice tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all freshservice tools with default credentials."""
        return get_freshservice_tools()
