# humanticai toolkit
from langchain.tools import BaseTool
from typing import List

def get_humanticai_tools() -> List[BaseTool]:
    """Get all humanticai tools."""
    from . import operations
    return operations.get_tools()

class HumanticaiToolkit:
    """Toolkit for interacting with humanticai."""

    def __init__(self):
        """Initialize the humanticai toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all humanticai tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all humanticai tools with default credentials."""
        return get_humanticai_tools()
