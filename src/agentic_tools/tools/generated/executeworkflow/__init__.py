# executeworkflow toolkit
from langchain.tools import BaseTool
from typing import List

def get_executeworkflow_tools() -> List[BaseTool]:
    """Get all executeworkflow tools."""
    from . import operations
    return operations.get_tools()

class ExecuteworkflowToolkit:
    """Toolkit for interacting with executeworkflow."""

    def __init__(self):
        """Initialize the executeworkflow toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all executeworkflow tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all executeworkflow tools with default credentials."""
        return get_executeworkflow_tools()
