# googleslides toolkit
from langchain.tools import BaseTool
from typing import List

def get_googleslides_tools() -> List[BaseTool]:
    """Get all googleslides tools."""
    from . import operations
    return operations.get_tools()

class GoogleslidesToolkit:
    """Toolkit for interacting with googleslides."""

    def __init__(self):
        """Initialize the googleslides toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googleslides tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googleslides tools with default credentials."""
        return get_googleslides_tools()
