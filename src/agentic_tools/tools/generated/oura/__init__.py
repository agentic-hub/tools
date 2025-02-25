# oura toolkit
from langchain.tools import BaseTool
from typing import List

def get_oura_tools() -> List[BaseTool]:
    """Get all oura tools."""
    from . import operations
    return operations.get_tools()

class OuraToolkit:
    """Toolkit for interacting with oura."""

    def __init__(self):
        """Initialize the oura toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all oura tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all oura tools with default credentials."""
        return get_oura_tools()
