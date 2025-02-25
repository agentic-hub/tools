# ical toolkit
from langchain.tools import BaseTool
from typing import List

def get_ical_tools() -> List[BaseTool]:
    """Get all ical tools."""
    from . import operations
    return operations.get_tools()

class IcalToolkit:
    """Toolkit for interacting with ical."""

    def __init__(self):
        """Initialize the ical toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all ical tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all ical tools with default credentials."""
        return get_ical_tools()
