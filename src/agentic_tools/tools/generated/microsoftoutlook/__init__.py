# microsoftoutlook toolkit
from langchain.tools import BaseTool
from typing import List

def get_microsoftoutlook_tools() -> List[BaseTool]:
    """Get all microsoftoutlook tools."""
    from . import operations
    return operations.get_tools()

class MicrosoftoutlookToolkit:
    """Toolkit for interacting with microsoftoutlook."""

    def __init__(self):
        """Initialize the microsoftoutlook toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all microsoftoutlook tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all microsoftoutlook tools with default credentials."""
        return get_microsoftoutlook_tools()
