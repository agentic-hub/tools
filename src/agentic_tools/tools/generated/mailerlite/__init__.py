# mailerlite toolkit
from langchain.tools import BaseTool
from typing import List

def get_mailerlite_tools() -> List[BaseTool]:
    """Get all mailerlite tools."""
    from . import operations
    return operations.get_tools()

class MailerliteToolkit:
    """Toolkit for interacting with mailerlite."""

    def __init__(self):
        """Initialize the mailerlite toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all mailerlite tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all mailerlite tools with default credentials."""
        return get_mailerlite_tools()
