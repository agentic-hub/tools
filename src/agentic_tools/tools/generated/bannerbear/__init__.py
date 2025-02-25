# bannerbear toolkit
from langchain.tools import BaseTool
from typing import List

def get_bannerbear_tools() -> List[BaseTool]:
    """Get all bannerbear tools."""
    from . import operations
    return operations.get_tools()

class BannerbearToolkit:
    """Toolkit for interacting with bannerbear."""

    def __init__(self):
        """Initialize the bannerbear toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all bannerbear tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all bannerbear tools with default credentials."""
        return get_bannerbear_tools()
