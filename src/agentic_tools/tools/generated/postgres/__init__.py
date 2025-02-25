# postgres toolkit
from langchain.tools import BaseTool
from typing import List

def get_postgres_tools() -> List[BaseTool]:
    """Get all postgres tools."""
    from . import operations
    return operations.get_tools()

class PostgresToolkit:
    """Toolkit for interacting with postgres."""

    def __init__(self):
        """Initialize the postgres toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all postgres tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all postgres tools with default credentials."""
        return get_postgres_tools()
