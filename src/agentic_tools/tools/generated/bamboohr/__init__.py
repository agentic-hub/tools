# bamboohr toolkit
from langchain.tools import BaseTool
from typing import List

def get_bamboohr_tools() -> List[BaseTool]:
    """Get all bamboohr tools."""
    from . import operations
    return operations.get_tools()

class BamboohrToolkit:
    """Toolkit for interacting with bamboohr."""

    def __init__(self):
        """Initialize the bamboohr toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all bamboohr tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all bamboohr tools with default credentials."""
        return get_bamboohr_tools()
