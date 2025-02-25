# mailcheck toolkit
from langchain.tools import BaseTool
from typing import List

def get_mailcheck_tools() -> List[BaseTool]:
    """Get all mailcheck tools."""
    from . import operations
    return operations.get_tools()

class MailcheckToolkit:
    """Toolkit for interacting with mailcheck."""

    def __init__(self):
        """Initialize the mailcheck toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all mailcheck tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all mailcheck tools with default credentials."""
        return get_mailcheck_tools()
