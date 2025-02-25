# respondtowebhook toolkit
from langchain.tools import BaseTool
from typing import List

def get_respondtowebhook_tools() -> List[BaseTool]:
    """Get all respondtowebhook tools."""
    from . import operations
    return operations.get_tools()

class RespondtowebhookToolkit:
    """Toolkit for interacting with respondtowebhook."""

    def __init__(self):
        """Initialize the respondtowebhook toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all respondtowebhook tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all respondtowebhook tools with default credentials."""
        return get_respondtowebhook_tools()
