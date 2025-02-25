# agilecrm toolkit
from langchain.tools import BaseTool
from typing import List

def get_agilecrm_tools() -> List[BaseTool]:
    """Get all agilecrm tools."""
    from . import operations
    return operations.get_tools()

class AgilecrmToolkit:
    """Toolkit for interacting with agilecrm."""

    def __init__(self):
        """Initialize the agilecrm toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all agilecrm tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all agilecrm tools with default credentials."""
        return get_agilecrm_tools()
