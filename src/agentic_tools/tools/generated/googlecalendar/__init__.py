# googlecalendar toolkit
from langchain.tools import BaseTool
from typing import List

def get_googlecalendar_tools() -> List[BaseTool]:
    """Get all googlecalendar tools."""
    from . import operations
    return operations.get_tools()

class GooglecalendarToolkit:
    """Toolkit for interacting with googlecalendar."""

    def __init__(self):
        """Initialize the googlecalendar toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googlecalendar tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googlecalendar tools with default credentials."""
        return get_googlecalendar_tools()
