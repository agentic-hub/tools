# lemlist toolkit
from langchain.tools import BaseTool
from typing import List

def get_lemlist_tools() -> List[BaseTool]:
    """Get all lemlist tools."""
    from . import operations
    return operations.get_tools()

class LemlistToolkit:
    """Toolkit for interacting with lemlist."""

    def __init__(self):
        """Initialize the lemlist toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all lemlist tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all lemlist tools with default credentials."""
        return get_lemlist_tools()
