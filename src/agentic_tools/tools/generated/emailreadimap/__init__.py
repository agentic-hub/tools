# emailreadimap toolkit
from langchain.tools import BaseTool
from typing import List

def get_emailreadimap_tools() -> List[BaseTool]:
    """Get all emailreadimap tools."""
    from . import operations
    return operations.get_tools()

class EmailreadimapToolkit:
    """Toolkit for interacting with emailreadimap."""

    def __init__(self):
        """Initialize the emailreadimap toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all emailreadimap tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all emailreadimap tools with default credentials."""
        return get_emailreadimap_tools()
