# clearbit toolkit
from langchain.tools import BaseTool
from typing import List

def get_clearbit_tools() -> List[BaseTool]:
    """Get all clearbit tools."""
    from . import operations
    return operations.get_tools()

class ClearbitToolkit:
    """Toolkit for interacting with clearbit."""

    def __init__(self):
        """Initialize the clearbit toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all clearbit tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all clearbit tools with default credentials."""
        return get_clearbit_tools()
