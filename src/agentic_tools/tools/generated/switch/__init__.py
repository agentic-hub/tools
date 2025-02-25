# switch toolkit
from langchain.tools import BaseTool
from typing import List

def get_switch_tools() -> List[BaseTool]:
    """Get all switch tools."""
    from . import operations
    return operations.get_tools()

class SwitchToolkit:
    """Toolkit for interacting with switch."""

    def __init__(self):
        """Initialize the switch toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all switch tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all switch tools with default credentials."""
        return get_switch_tools()
