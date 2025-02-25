# thehive toolkit
from langchain.tools import BaseTool
from typing import List

def get_thehive_tools() -> List[BaseTool]:
    """Get all thehive tools."""
    from . import operations
    return operations.get_tools()

class ThehiveToolkit:
    """Toolkit for interacting with thehive."""

    def __init__(self):
        """Initialize the thehive toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all thehive tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all thehive tools with default credentials."""
        return get_thehive_tools()
