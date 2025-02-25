# lonescale toolkit
from langchain.tools import BaseTool
from typing import List

def get_lonescale_tools() -> List[BaseTool]:
    """Get all lonescale tools."""
    from . import operations
    return operations.get_tools()

class LonescaleToolkit:
    """Toolkit for interacting with lonescale."""

    def __init__(self):
        """Initialize the lonescale toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all lonescale tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all lonescale tools with default credentials."""
        return get_lonescale_tools()
