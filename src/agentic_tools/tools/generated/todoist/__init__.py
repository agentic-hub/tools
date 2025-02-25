# todoist toolkit
from langchain.tools import BaseTool
from typing import List

def get_todoist_tools() -> List[BaseTool]:
    """Get all todoist tools."""
    from . import operations
    return operations.get_tools()

class TodoistToolkit:
    """Toolkit for interacting with todoist."""

    def __init__(self):
        """Initialize the todoist toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all todoist tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all todoist tools with default credentials."""
        return get_todoist_tools()
