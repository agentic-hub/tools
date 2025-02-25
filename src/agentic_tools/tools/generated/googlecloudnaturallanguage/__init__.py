# googlecloudnaturallanguage toolkit
from langchain.tools import BaseTool
from typing import List

def get_googlecloudnaturallanguage_tools() -> List[BaseTool]:
    """Get all googlecloudnaturallanguage tools."""
    from . import operations
    return operations.get_tools()

class GooglecloudnaturallanguageToolkit:
    """Toolkit for interacting with googlecloudnaturallanguage."""

    def __init__(self):
        """Initialize the googlecloudnaturallanguage toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googlecloudnaturallanguage tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googlecloudnaturallanguage tools with default credentials."""
        return get_googlecloudnaturallanguage_tools()
