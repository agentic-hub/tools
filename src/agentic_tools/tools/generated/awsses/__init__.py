# awsses toolkit
from langchain.tools import BaseTool
from typing import List

def get_awsses_tools() -> List[BaseTool]:
    """Get all awsses tools."""
    from . import operations
    return operations.get_tools()

class AwsSesToolkit:
    """Toolkit for interacting with awsses."""

    def __init__(self):
        """Initialize the awsses toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all awsses tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all awsses tools with default credentials."""
        return get_awsses_tools()
