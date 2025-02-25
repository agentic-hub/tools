# servicenow toolkit
from langchain.tools import BaseTool
from typing import List

def get_servicenow_tools() -> List[BaseTool]:
    """Get all servicenow tools."""
    from . import operations
    return operations.get_tools()

class ServicenowToolkit:
    """Toolkit for interacting with servicenow."""

    def __init__(self):
        """Initialize the servicenow toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all servicenow tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all servicenow tools with default credentials."""
        return get_servicenow_tools()
