# affinity toolkit
from langchain.tools import BaseTool
from typing import List

def get_affinity_tools() -> List[BaseTool]:
    """Get all affinity tools."""
    from . import operations
    return operations.get_tools()

class AffinityToolkit:
    """Toolkit for interacting with affinity."""

    def __init__(self):
        """Initialize the affinity toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all affinity tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all affinity tools with default credentials."""
        return get_affinity_tools()
