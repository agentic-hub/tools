# gmail toolkit
from langchain.tools import BaseTool
from typing import List

def get_gmail_tools() -> List[BaseTool]:
    """Get all gmail tools."""
    from . import operations
    return operations.get_tools()

class GmailToolkit:
    """Toolkit for interacting with gmail."""

    def __init__(self):
        """Initialize the gmail toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all gmail tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all gmail tools with default credentials."""
        return get_gmail_tools()
