# magento2 toolkit
from langchain.tools import BaseTool
from typing import List

def get_magento2_tools() -> List[BaseTool]:
    """Get all magento2 tools."""
    from . import operations
    return operations.get_tools()

class MagentoToolkit:
    """Toolkit for interacting with magento2."""

    def __init__(self):
        """Initialize the magento2 toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all magento2 tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all magento2 tools with default credentials."""
        return get_magento2_tools()
