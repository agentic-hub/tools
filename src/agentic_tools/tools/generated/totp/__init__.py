# totp toolkit
from langchain.tools import BaseTool
from typing import List

def get_totp_tools() -> List[BaseTool]:
    """Get all totp tools."""
    from . import operations
    return operations.get_tools()

class TotpToolkit:
    """Toolkit for interacting with totp."""

    def __init__(self):
        """Initialize the totp toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all totp tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all totp tools with default credentials."""
        return get_totp_tools()
