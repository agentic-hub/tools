# posthog toolkit
from langchain.tools import BaseTool
from typing import List

def get_posthog_tools() -> List[BaseTool]:
    """Get all posthog tools."""
    from . import operations
    return operations.get_tools()

class PosthogToolkit:
    """Toolkit for interacting with posthog."""

    def __init__(self):
        """Initialize the posthog toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all posthog tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all posthog tools with default credentials."""
        return get_posthog_tools()
