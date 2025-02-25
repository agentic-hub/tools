# crowddev toolkit
from langchain.tools import BaseTool
from typing import List

def get_crowddev_tools() -> List[BaseTool]:
    """Get all crowddev tools."""
    from . import operations
    return operations.get_tools()

class CrowddevToolkit:
    """Toolkit for interacting with crowddev."""

    def __init__(self):
        """Initialize the crowddev toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all crowddev tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all crowddev tools with default credentials."""
        return get_crowddev_tools()
