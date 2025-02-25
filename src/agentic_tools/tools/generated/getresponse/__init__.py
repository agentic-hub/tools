# getresponse toolkit
from langchain.tools import BaseTool
from typing import List

def get_getresponse_tools() -> List[BaseTool]:
    """Get all getresponse tools."""
    from . import operations
    return operations.get_tools()

class GetresponseToolkit:
    """Toolkit for interacting with getresponse."""

    def __init__(self):
        """Initialize the getresponse toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all getresponse tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all getresponse tools with default credentials."""
        return get_getresponse_tools()
