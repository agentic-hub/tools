# venafitlsprotectdatacenter toolkit
from langchain.tools import BaseTool
from typing import List

def get_venafitlsprotectdatacenter_tools() -> List[BaseTool]:
    """Get all venafitlsprotectdatacenter tools."""
    from . import operations
    return operations.get_tools()

class VenafitlsprotectdatacenterToolkit:
    """Toolkit for interacting with venafitlsprotectdatacenter."""

    def __init__(self):
        """Initialize the venafitlsprotectdatacenter toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all venafitlsprotectdatacenter tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all venafitlsprotectdatacenter tools with default credentials."""
        return get_venafitlsprotectdatacenter_tools()
