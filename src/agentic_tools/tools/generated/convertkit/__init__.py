# convertkit toolkit
from langchain.tools import BaseTool
from typing import List

def get_convertkit_tools() -> List[BaseTool]:
    """Get all convertkit tools."""
    from . import operations
    return operations.get_tools()

class ConvertkitToolkit:
    """Toolkit for interacting with convertkit."""

    def __init__(self):
        """Initialize the convertkit toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all convertkit tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all convertkit tools with default credentials."""
        return get_convertkit_tools()
