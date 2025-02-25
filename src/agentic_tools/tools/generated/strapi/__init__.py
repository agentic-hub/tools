# strapi toolkit
from langchain.tools import BaseTool
from typing import List

def get_strapi_tools() -> List[BaseTool]:
    """Get all strapi tools."""
    from . import operations
    return operations.get_tools()

class StrapiToolkit:
    """Toolkit for interacting with strapi."""

    def __init__(self):
        """Initialize the strapi toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all strapi tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all strapi tools with default credentials."""
        return get_strapi_tools()
