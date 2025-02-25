# profitwell toolkit
from langchain.tools import BaseTool
from typing import List

def get_profitwell_tools() -> List[BaseTool]:
    """Get all profitwell tools."""
    from . import operations
    return operations.get_tools()

class ProfitwellToolkit:
    """Toolkit for interacting with profitwell."""

    def __init__(self):
        """Initialize the profitwell toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all profitwell tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all profitwell tools with default credentials."""
        return get_profitwell_tools()
