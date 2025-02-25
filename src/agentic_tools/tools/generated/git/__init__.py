# git toolkit
from langchain.tools import BaseTool
from typing import List

def get_git_tools() -> List[BaseTool]:
    """Get all git tools."""
    from . import operations
    return operations.get_tools()

class GitToolkit:
    """Toolkit for interacting with git."""

    def __init__(self):
        """Initialize the git toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all git tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all git tools with default credentials."""
        return get_git_tools()
