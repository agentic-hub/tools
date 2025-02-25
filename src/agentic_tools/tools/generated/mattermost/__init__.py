# mattermost toolkit
from langchain.tools import BaseTool
from typing import List

def get_mattermost_tools() -> List[BaseTool]:
    """Get all mattermost tools."""
    from . import operations
    return operations.get_tools()

class MattermostToolkit:
    """Toolkit for interacting with mattermost."""

    def __init__(self):
        """Initialize the mattermost toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all mattermost tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all mattermost tools with default credentials."""
        return get_mattermost_tools()
