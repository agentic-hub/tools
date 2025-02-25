# erpnext toolkit
from langchain.tools import BaseTool
from typing import List

def get_erpnext_tools() -> List[BaseTool]:
    """Get all erpnext tools."""
    from . import operations
    return operations.get_tools()

class ErpnextToolkit:
    """Toolkit for interacting with erpnext."""

    def __init__(self):
        """Initialize the erpnext toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all erpnext tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all erpnext tools with default credentials."""
        return get_erpnext_tools()
