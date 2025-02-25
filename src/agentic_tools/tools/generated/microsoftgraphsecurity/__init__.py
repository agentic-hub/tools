# microsoftgraphsecurity toolkit
from langchain.tools import BaseTool
from typing import List

def get_microsoftgraphsecurity_tools() -> List[BaseTool]:
    """Get all microsoftgraphsecurity tools."""
    from . import operations
    return operations.get_tools()

class MicrosoftgraphsecurityToolkit:
    """Toolkit for interacting with microsoftgraphsecurity."""

    def __init__(self):
        """Initialize the microsoftgraphsecurity toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all microsoftgraphsecurity tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all microsoftgraphsecurity tools with default credentials."""
        return get_microsoftgraphsecurity_tools()
