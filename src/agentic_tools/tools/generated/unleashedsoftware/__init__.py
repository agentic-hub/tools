# unleashedsoftware toolkit
from langchain.tools import BaseTool
from typing import List

def get_unleashedsoftware_tools() -> List[BaseTool]:
    """Get all unleashedsoftware tools."""
    from . import operations
    return operations.get_tools()

class UnleashedsoftwareToolkit:
    """Toolkit for interacting with unleashedsoftware."""

    def __init__(self):
        """Initialize the unleashedsoftware toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all unleashedsoftware tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all unleashedsoftware tools with default credentials."""
        return get_unleashedsoftware_tools()
