# github toolkit
from langchain.tools import BaseTool
from typing import List

def get_github_tools() -> List[BaseTool]:
    """Get all github tools."""
    from . import operations
    return operations.get_tools()

class GithubToolkit:
    """Toolkit for interacting with github."""

    def __init__(self):
        """Initialize the github toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all github tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all github tools with default credentials."""
        return get_github_tools()
