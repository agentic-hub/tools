# clickup toolkit
from langchain.tools import BaseTool
from typing import List

def get_clickup_tools() -> List[BaseTool]:
    """Get all clickup tools."""
    from . import operations
    return operations.get_tools()

class ClickupToolkit:
    """Toolkit for interacting with clickup."""

    def __init__(self):
        """Initialize the clickup toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all clickup tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all clickup tools with default credentials."""
        return get_clickup_tools()
