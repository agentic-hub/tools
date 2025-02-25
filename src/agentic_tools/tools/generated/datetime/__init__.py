# datetime toolkit
from langchain.tools import BaseTool
from typing import List

def get_datetime_tools() -> List[BaseTool]:
    """Get all datetime tools."""
    from . import operations
    return operations.get_tools()

class DatetimeToolkit:
    """Toolkit for interacting with datetime."""

    def __init__(self):
        """Initialize the datetime toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all datetime tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all datetime tools with default credentials."""
        return get_datetime_tools()
