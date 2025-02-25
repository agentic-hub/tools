# webflow toolkit
from langchain.tools import BaseTool
from typing import List

def get_webflow_tools() -> List[BaseTool]:
    """Get all webflow tools."""
    from . import operations
    return operations.get_tools()

class WebflowToolkit:
    """Toolkit for interacting with webflow."""

    def __init__(self):
        """Initialize the webflow toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all webflow tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all webflow tools with default credentials."""
        return get_webflow_tools()
