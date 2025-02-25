# cloudflare toolkit
from langchain.tools import BaseTool
from typing import List

def get_cloudflare_tools() -> List[BaseTool]:
    """Get all cloudflare tools."""
    from . import operations
    return operations.get_tools()

class CloudflareToolkit:
    """Toolkit for interacting with cloudflare."""

    def __init__(self):
        """Initialize the cloudflare toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all cloudflare tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all cloudflare tools with default credentials."""
        return get_cloudflare_tools()
