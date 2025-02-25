# googlebigquery toolkit
from langchain.tools import BaseTool
from typing import List

def get_googlebigquery_tools() -> List[BaseTool]:
    """Get all googlebigquery tools."""
    from . import operations
    return operations.get_tools()

class GooglebigqueryToolkit:
    """Toolkit for interacting with googlebigquery."""

    def __init__(self):
        """Initialize the googlebigquery toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googlebigquery tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googlebigquery tools with default credentials."""
        return get_googlebigquery_tools()
