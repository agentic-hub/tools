# zohocrm toolkit
from langchain.tools import BaseTool
from typing import List

def get_zohocrm_tools() -> List[BaseTool]:
    """Get all zohocrm tools."""
    from . import operations
    return operations.get_tools()

class ZohocrmToolkit:
    """Toolkit for interacting with zohocrm."""

    def __init__(self):
        """Initialize the zohocrm toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all zohocrm tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all zohocrm tools with default credentials."""
        return get_zohocrm_tools()
