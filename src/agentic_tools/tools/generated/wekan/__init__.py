# wekan toolkit
from langchain.tools import BaseTool
from typing import List

def get_wekan_tools() -> List[BaseTool]:
    """Get all wekan tools."""
    from . import operations
    return operations.get_tools()

class WekanToolkit:
    """Toolkit for interacting with wekan."""

    def __init__(self):
        """Initialize the wekan toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all wekan tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all wekan tools with default credentials."""
        return get_wekan_tools()
