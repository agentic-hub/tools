# venafitlsprotectcloud toolkit
from langchain.tools import BaseTool
from typing import List

def get_venafitlsprotectcloud_tools() -> List[BaseTool]:
    """Get all venafitlsprotectcloud tools."""
    from . import operations
    return operations.get_tools()

class VenafitlsprotectcloudToolkit:
    """Toolkit for interacting with venafitlsprotectcloud."""

    def __init__(self):
        """Initialize the venafitlsprotectcloud toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all venafitlsprotectcloud tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all venafitlsprotectcloud tools with default credentials."""
        return get_venafitlsprotectcloud_tools()
