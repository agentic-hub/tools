# webhook toolkit
from langchain.tools import BaseTool
from typing import List

def get_webhook_tools() -> List[BaseTool]:
    """Get all webhook tools."""
    from . import operations
    return operations.get_tools()

class WebhookToolkit:
    """Toolkit for interacting with webhook."""

    def __init__(self):
        """Initialize the webhook toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all webhook tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all webhook tools with default credentials."""
        return get_webhook_tools()
