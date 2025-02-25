# philipshue toolkit
from langchain.tools import BaseTool
from typing import List

def get_philipshue_tools() -> List[BaseTool]:
    """Get all philipshue tools."""
    from . import operations
    return operations.get_tools()

class PhilipshueToolkit:
    """Toolkit for interacting with philipshue."""

    def __init__(self):
        """Initialize the philipshue toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all philipshue tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all philipshue tools with default credentials."""
        return get_philipshue_tools()
