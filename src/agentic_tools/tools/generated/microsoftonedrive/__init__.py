# microsoftonedrive toolkit
from langchain.tools import BaseTool
from typing import List

def get_microsoftonedrive_tools() -> List[BaseTool]:
    """Get all microsoftonedrive tools."""
    from . import operations
    return operations.get_tools()

class MicrosoftonedriveToolkit:
    """Toolkit for interacting with microsoftonedrive."""

    def __init__(self):
        """Initialize the microsoftonedrive toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all microsoftonedrive tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all microsoftonedrive tools with default credentials."""
        return get_microsoftonedrive_tools()
