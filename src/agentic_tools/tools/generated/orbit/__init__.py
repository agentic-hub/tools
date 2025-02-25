# orbit toolkit
from langchain.tools import BaseTool
from typing import List

def get_orbit_tools() -> List[BaseTool]:
    """Get all orbit tools."""
    from . import operations
    return operations.get_tools()

class OrbitToolkit:
    """Toolkit for interacting with orbit."""

    def __init__(self):
        """Initialize the orbit toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all orbit tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all orbit tools with default credentials."""
        return get_orbit_tools()
