# awssqs toolkit
from langchain.tools import BaseTool
from typing import List

def get_awssqs_tools() -> List[BaseTool]:
    """Get all awssqs tools."""
    from . import operations
    return operations.get_tools()

class AwsSqsToolkit:
    """Toolkit for interacting with awssqs."""

    def __init__(self):
        """Initialize the awssqs toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all awssqs tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all awssqs tools with default credentials."""
        return get_awssqs_tools()
