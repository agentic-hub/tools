# bitwarden toolkit
from langchain.tools import BaseTool
from typing import List

def get_bitwarden_tools() -> List[BaseTool]:
    """Get all bitwarden tools."""
    from . import operations
    return operations.get_tools()

class BitwardenToolkit:
    """Toolkit for interacting with bitwarden."""

    def __init__(self):
        """Initialize the bitwarden toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all bitwarden tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all bitwarden tools with default credentials."""
        return get_bitwarden_tools()
