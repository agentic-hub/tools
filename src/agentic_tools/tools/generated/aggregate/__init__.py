# aggregate toolkit
from langchain.tools import BaseTool
from typing import List

def get_aggregate_tools() -> List[BaseTool]:
    """Get all aggregate tools."""
    from . import operations
    return operations.get_tools()

class AggregateToolkit:
    """Toolkit for interacting with aggregate."""

    def __init__(self):
        """Initialize the aggregate toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all aggregate tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all aggregate tools with default credentials."""
        return get_aggregate_tools()
