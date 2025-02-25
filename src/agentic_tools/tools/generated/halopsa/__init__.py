# halopsa toolkit
from langchain.tools import BaseTool
from typing import List

def get_halopsa_tools() -> List[BaseTool]:
    """Get all halopsa tools."""
    from . import operations
    return operations.get_tools()

class HalopsaToolkit:
    """Toolkit for interacting with halopsa."""

    def __init__(self):
        """Initialize the halopsa toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all halopsa tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all halopsa tools with default credentials."""
        return get_halopsa_tools()
