# zulip toolkit
from langchain.tools import BaseTool
from typing import List

def get_zulip_tools() -> List[BaseTool]:
    """Get all zulip tools."""
    from . import operations
    return operations.get_tools()

class ZulipToolkit:
    """Toolkit for interacting with zulip."""

    def __init__(self):
        """Initialize the zulip toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all zulip tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all zulip tools with default credentials."""
        return get_zulip_tools()
