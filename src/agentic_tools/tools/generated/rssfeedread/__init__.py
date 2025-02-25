# rssfeedread toolkit
from langchain.tools import BaseTool
from typing import List

def get_rssfeedread_tools() -> List[BaseTool]:
    """Get all rssfeedread tools."""
    from . import operations
    return operations.get_tools()

class RssfeedreadToolkit:
    """Toolkit for interacting with rssfeedread."""

    def __init__(self):
        """Initialize the rssfeedread toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all rssfeedread tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all rssfeedread tools with default credentials."""
        return get_rssfeedread_tools()
