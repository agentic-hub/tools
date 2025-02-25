# slack toolkit
from langchain.tools import BaseTool
from typing import List

def get_slack_tools() -> List[BaseTool]:
    """Get all slack tools."""
    from . import operations
    return operations.get_tools()

class SlackToolkit:
    """Toolkit for interacting with slack."""

    def __init__(self):
        """Initialize the slack toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all slack tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all slack tools with default credentials."""
        return get_slack_tools()
