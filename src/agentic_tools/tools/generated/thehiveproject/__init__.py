# thehiveproject toolkit
from langchain.tools import BaseTool
from typing import List

def get_thehiveproject_tools() -> List[BaseTool]:
    """Get all thehiveproject tools."""
    from . import operations
    return operations.get_tools()

class ThehiveprojectToolkit:
    """Toolkit for interacting with thehiveproject."""

    def __init__(self):
        """Initialize the thehiveproject toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all thehiveproject tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all thehiveproject tools with default credentials."""
        return get_thehiveproject_tools()
