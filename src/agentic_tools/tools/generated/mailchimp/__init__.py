# mailchimp toolkit
from langchain.tools import BaseTool
from typing import List

def get_mailchimp_tools() -> List[BaseTool]:
    """Get all mailchimp tools."""
    from . import operations
    return operations.get_tools()

class MailchimpToolkit:
    """Toolkit for interacting with mailchimp."""

    def __init__(self):
        """Initialize the mailchimp toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all mailchimp tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all mailchimp tools with default credentials."""
        return get_mailchimp_tools()
