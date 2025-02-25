# intercom toolkit
from langchain.tools import BaseTool
from typing import List

def get_intercom_tools() -> List[BaseTool]:
    """Get all intercom tools."""
    from . import operations
    return operations.get_tools()

class IntercomToolkit:
    """Toolkit for interacting with intercom."""

    def __init__(self):
        """Initialize the intercom toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all intercom tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all intercom tools with default credentials."""
        return get_intercom_tools()
