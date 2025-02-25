# box toolkit
from langchain.tools import BaseTool
from typing import List

def get_box_tools() -> List[BaseTool]:
    """Get all box tools."""
    from . import operations
    return operations.get_tools()

class BoxToolkit:
    """Toolkit for interacting with box."""

    def __init__(self):
        """Initialize the box toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all box tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all box tools with default credentials."""
        return get_box_tools()
