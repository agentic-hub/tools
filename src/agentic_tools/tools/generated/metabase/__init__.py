# metabase toolkit
from langchain.tools import BaseTool
from typing import List

def get_metabase_tools() -> List[BaseTool]:
    """Get all metabase tools."""
    from . import operations
    return operations.get_tools()

class MetabaseToolkit:
    """Toolkit for interacting with metabase."""

    def __init__(self):
        """Initialize the metabase toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all metabase tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all metabase tools with default credentials."""
        return get_metabase_tools()
