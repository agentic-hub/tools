# emelia toolkit
from langchain.tools import BaseTool
from typing import List

def get_emelia_tools() -> List[BaseTool]:
    """Get all emelia tools."""
    from . import operations
    return operations.get_tools()

class EmeliaToolkit:
    """Toolkit for interacting with emelia."""

    def __init__(self):
        """Initialize the emelia toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all emelia tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all emelia tools with default credentials."""
        return get_emelia_tools()
