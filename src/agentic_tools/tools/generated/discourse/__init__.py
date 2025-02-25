# discourse toolkit
from langchain.tools import BaseTool
from typing import List

def get_discourse_tools() -> List[BaseTool]:
    """Get all discourse tools."""
    from . import operations
    return operations.get_tools()

class DiscourseToolkit:
    """Toolkit for interacting with discourse."""

    def __init__(self):
        """Initialize the discourse toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all discourse tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all discourse tools with default credentials."""
        return get_discourse_tools()
