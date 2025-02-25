# awscertificatemanager toolkit
from langchain.tools import BaseTool
from typing import List

def get_awscertificatemanager_tools() -> List[BaseTool]:
    """Get all awscertificatemanager tools."""
    from . import operations
    return operations.get_tools()

class AwsCertificatemanagerToolkit:
    """Toolkit for interacting with awscertificatemanager."""

    def __init__(self):
        """Initialize the awscertificatemanager toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all awscertificatemanager tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all awscertificatemanager tools with default credentials."""
        return get_awscertificatemanager_tools()
