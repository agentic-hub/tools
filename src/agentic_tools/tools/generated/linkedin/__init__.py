# linkedin toolkit
from langchain.tools import BaseTool
from typing import List

def get_linkedin_tools() -> List[BaseTool]:
    """Get all linkedin tools."""
    from . import operations
    return operations.get_tools()

class LinkedinToolkit:
    """Toolkit for interacting with linkedin."""

    def __init__(self):
        """Initialize the linkedin toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all linkedin tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all linkedin tools with default credentials."""
        return get_linkedin_tools()
