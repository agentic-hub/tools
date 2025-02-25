# shopify toolkit
from langchain.tools import BaseTool
from typing import List

def get_shopify_tools() -> List[BaseTool]:
    """Get all shopify tools."""
    from . import operations
    return operations.get_tools()

class ShopifyToolkit:
    """Toolkit for interacting with shopify."""

    def __init__(self):
        """Initialize the shopify toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all shopify tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all shopify tools with default credentials."""
        return get_shopify_tools()
