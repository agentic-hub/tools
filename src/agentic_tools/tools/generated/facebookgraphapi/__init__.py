# facebookgraphapi toolkit
from langchain.tools import BaseTool
from typing import List

def get_facebookgraphapi_tools() -> List[BaseTool]:
    """Get all facebookgraphapi tools."""
    from . import operations
    return operations.get_tools()

class FacebookgraphapiToolkit:
    """Toolkit for interacting with facebookgraphapi."""

    def __init__(self):
        """Initialize the facebookgraphapi toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all facebookgraphapi tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all facebookgraphapi tools with default credentials."""
        return get_facebookgraphapi_tools()
