# nocodb toolkit
from langchain.tools import BaseTool
from typing import List

def get_nocodb_tools() -> List[BaseTool]:
    """Get all nocodb tools."""
    from . import operations
    return operations.get_tools()

class NocodbToolkit:
    """Toolkit for interacting with nocodb."""

    def __init__(self):
        """Initialize the nocodb toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all nocodb tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all nocodb tools with default credentials."""
        return get_nocodb_tools()
