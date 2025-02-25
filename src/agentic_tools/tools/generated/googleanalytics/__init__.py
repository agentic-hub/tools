# googleanalytics toolkit
from langchain.tools import BaseTool
from typing import List

def get_googleanalytics_tools() -> List[BaseTool]:
    """Get all googleanalytics tools."""
    from . import operations
    return operations.get_tools()

class GoogleanalyticsToolkit:
    """Toolkit for interacting with googleanalytics."""

    def __init__(self):
        """Initialize the googleanalytics toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all googleanalytics tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all googleanalytics tools with default credentials."""
        return get_googleanalytics_tools()
