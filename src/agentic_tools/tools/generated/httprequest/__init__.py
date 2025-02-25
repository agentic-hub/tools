# httprequest toolkit
from langchain.tools import BaseTool
from typing import List

def get_httprequest_tools() -> List[BaseTool]:
    """Get all httprequest tools."""
    from . import operations
    return operations.get_tools()

class HttprequestToolkit:
    """Toolkit for interacting with httprequest."""

    def __init__(self):
        """Initialize the httprequest toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all httprequest tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all httprequest tools with default credentials."""
        return get_httprequest_tools()
