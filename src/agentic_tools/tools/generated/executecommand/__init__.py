# executecommand toolkit
from langchain.tools import BaseTool
from typing import List

def get_executecommand_tools() -> List[BaseTool]:
    """Get all executecommand tools."""
    from . import operations
    return operations.get_tools()

class ExecutecommandToolkit:
    """Toolkit for interacting with executecommand."""

    def __init__(self):
        """Initialize the executecommand toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all executecommand tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all executecommand tools with default credentials."""
        return get_executecommand_tools()
