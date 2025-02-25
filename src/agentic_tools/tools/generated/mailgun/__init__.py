# mailgun toolkit
from langchain.tools import BaseTool
from typing import List

def get_mailgun_tools() -> List[BaseTool]:
    """Get all mailgun tools."""
    from . import operations
    return operations.get_tools()

class MailgunToolkit:
    """Toolkit for interacting with mailgun."""

    def __init__(self):
        """Initialize the mailgun toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all mailgun tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all mailgun tools with default credentials."""
        return get_mailgun_tools()
