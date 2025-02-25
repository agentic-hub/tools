# noop toolkit
from langchain.tools import BaseTool
from typing import List

def get_noop_tools() -> List[BaseTool]:
    """Get all noop tools."""
    from . import operations
    return operations.get_tools()

class NoopToolkit:
    """Toolkit for interacting with noop."""

    def __init__(self):
        """Initialize the noop toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all noop tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all noop tools with default credentials."""
        return get_noop_tools()
