# googletranslate toolkit
from langchain.tools import BaseTool
from typing import List

def get_googletranslate_tools() -> List[BaseTool]:
    """Get all googletranslate tools."""
    from . import operations
    return operations.get_tools()

class GoogletranslateToolkit:
    """Toolkit for interacting with googletranslate."""

    def __init__(self):
        """Initialize the googletranslate toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googletranslate tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googletranslate tools with default credentials."""
        return get_googletranslate_tools()
