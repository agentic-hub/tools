# mailjet toolkit
from langchain.tools import BaseTool
from typing import List

def get_mailjet_tools() -> List[BaseTool]:
    """Get all mailjet tools."""
    from . import operations
    return operations.get_tools()

class MailjetToolkit:
    """Toolkit for interacting with mailjet."""

    def __init__(self):
        """Initialize the mailjet toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all mailjet tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all mailjet tools with default credentials."""
        return get_mailjet_tools()
