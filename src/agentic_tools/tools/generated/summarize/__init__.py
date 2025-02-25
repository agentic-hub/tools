# summarize toolkit
from langchain.tools import BaseTool
from typing import List

def get_summarize_tools() -> List[BaseTool]:
    """Get all summarize tools."""
    from . import operations
    return operations.get_tools()

class SummarizeToolkit:
    """Toolkit for interacting with summarize."""

    def __init__(self):
        """Initialize the summarize toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all summarize tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all summarize tools with default credentials."""
        return get_summarize_tools()
