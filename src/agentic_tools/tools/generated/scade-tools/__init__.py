# scade-tools toolkit
from langchain.tools import BaseTool
from typing import List

def get_scade-tools_tools() -> List[BaseTool]:
    """Get all scade-tools tools."""
    from . import operations
    return operations.get_tools()

class ScadeToolsToolkit:
    """Toolkit for interacting with scade-tools."""

    def __init__(self):
        """Initialize the scade-tools toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all scade-tools tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all scade-tools tools with default credentials."""
        return get_scade-tools_tools()
