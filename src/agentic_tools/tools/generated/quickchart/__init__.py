# quickchart toolkit
from langchain.tools import BaseTool
from typing import List

def get_quickchart_tools() -> List[BaseTool]:
    """Get all quickchart tools."""
    from . import operations
    return operations.get_tools()

class QuickchartToolkit:
    """Toolkit for interacting with quickchart."""

    def __init__(self):
        """Initialize the quickchart toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all quickchart tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all quickchart tools with default credentials."""
        return get_quickchart_tools()
