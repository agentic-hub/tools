# line toolkit
from langchain.tools import BaseTool
from typing import List

def get_line_tools() -> List[BaseTool]:
    """Get all line tools."""
    from . import operations
    return operations.get_tools()

class LineToolkit:
    """Toolkit for interacting with line."""

    def __init__(self):
        """Initialize the line toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all line tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all line tools with default credentials."""
        return get_line_tools()
