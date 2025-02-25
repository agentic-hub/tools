# messagebird toolkit
from langchain.tools import BaseTool
from typing import List

def get_messagebird_tools() -> List[BaseTool]:
    """Get all messagebird tools."""
    from . import operations
    return operations.get_tools()

class MessagebirdToolkit:
    """Toolkit for interacting with messagebird."""

    def __init__(self):
        """Initialize the messagebird toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all messagebird tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all messagebird tools with default credentials."""
        return get_messagebird_tools()
