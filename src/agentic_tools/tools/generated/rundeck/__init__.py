# rundeck toolkit
from langchain.tools import BaseTool
from typing import List

def get_rundeck_tools() -> List[BaseTool]:
    """Get all rundeck tools."""
    from . import operations
    return operations.get_tools()

class RundeckToolkit:
    """Toolkit for interacting with rundeck."""

    def __init__(self):
        """Initialize the rundeck toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all rundeck tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all rundeck tools with default credentials."""
        return get_rundeck_tools()
