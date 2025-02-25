# gitlab toolkit
from langchain.tools import BaseTool
from typing import List

def get_gitlab_tools() -> List[BaseTool]:
    """Get all gitlab tools."""
    from . import operations
    return operations.get_tools()

class GitlabToolkit:
    """Toolkit for interacting with gitlab."""

    def __init__(self):
        """Initialize the gitlab toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all gitlab tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all gitlab tools with default credentials."""
        return get_gitlab_tools()
