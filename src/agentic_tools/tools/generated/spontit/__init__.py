# spontit toolkit
from langchain.tools import BaseTool
from typing import List

def get_spontit_tools() -> List[BaseTool]:
    """Get all spontit tools."""
    from . import operations
    return operations.get_tools()

class SpontitToolkit:
    """Toolkit for interacting with spontit."""

    def __init__(self):
        """Initialize the spontit toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all spontit tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all spontit tools with default credentials."""
        return get_spontit_tools()
