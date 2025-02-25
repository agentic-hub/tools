# coda toolkit
from langchain.tools import BaseTool
from typing import List

def get_coda_tools() -> List[BaseTool]:
    """Get all coda tools."""
    from . import operations
    return operations.get_tools()

class CodaToolkit:
    """Toolkit for interacting with coda."""

    def __init__(self):
        """Initialize the coda toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all coda tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all coda tools with default credentials."""
        return get_coda_tools()
