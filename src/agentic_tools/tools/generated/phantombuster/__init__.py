# phantombuster toolkit
from langchain.tools import BaseTool
from typing import List

def get_phantombuster_tools() -> List[BaseTool]:
    """Get all phantombuster tools."""
    from . import operations
    return operations.get_tools()

class PhantombusterToolkit:
    """Toolkit for interacting with phantombuster."""

    def __init__(self):
        """Initialize the phantombuster toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all phantombuster tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all phantombuster tools with default credentials."""
        return get_phantombuster_tools()
