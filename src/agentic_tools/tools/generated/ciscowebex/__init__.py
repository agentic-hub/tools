# ciscowebex toolkit
from langchain.tools import BaseTool
from typing import List

def get_ciscowebex_tools() -> List[BaseTool]:
    """Get all ciscowebex tools."""
    from . import operations
    return operations.get_tools()

class CiscowebexToolkit:
    """Toolkit for interacting with ciscowebex."""

    def __init__(self):
        """Initialize the ciscowebex toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all ciscowebex tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all ciscowebex tools with default credentials."""
        return get_ciscowebex_tools()
