# sendy toolkit
from langchain.tools import BaseTool
from typing import List

def get_sendy_tools() -> List[BaseTool]:
    """Get all sendy tools."""
    from . import operations
    return operations.get_tools()

class SendyToolkit:
    """Toolkit for interacting with sendy."""

    def __init__(self):
        """Initialize the sendy toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all sendy tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all sendy tools with default credentials."""
        return get_sendy_tools()
