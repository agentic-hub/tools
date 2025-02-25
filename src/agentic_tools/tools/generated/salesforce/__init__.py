# salesforce toolkit
from langchain.tools import BaseTool
from typing import List

def get_salesforce_tools() -> List[BaseTool]:
    """Get all salesforce tools."""
    from . import operations
    return operations.get_tools()

class SalesforceToolkit:
    """Toolkit for interacting with salesforce."""

    def __init__(self):
        """Initialize the salesforce toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all salesforce tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all salesforce tools with default credentials."""
        return get_salesforce_tools()
