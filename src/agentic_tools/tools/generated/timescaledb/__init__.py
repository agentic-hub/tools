# timescaledb toolkit
from langchain.tools import BaseTool
from typing import List

def get_timescaledb_tools() -> List[BaseTool]:
    """Get all timescaledb tools."""
    from . import operations
    return operations.get_tools()

class TimescaledbToolkit:
    """Toolkit for interacting with timescaledb."""

    def __init__(self):
        """Initialize the timescaledb toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all timescaledb tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all timescaledb tools with default credentials."""
        return get_timescaledb_tools()
