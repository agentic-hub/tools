# kobotoolbox toolkit
from langchain.tools import BaseTool
from typing import List

def get_kobotoolbox_tools() -> List[BaseTool]:
    """Get all kobotoolbox tools."""
    from . import operations
    return operations.get_tools()

class KobotoolboxToolkit:
    """Toolkit for interacting with kobotoolbox."""

    def __init__(self):
        """Initialize the kobotoolbox toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all kobotoolbox tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all kobotoolbox tools with default credentials."""
        return get_kobotoolbox_tools()
