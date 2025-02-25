# awsdynamodb toolkit
from langchain.tools import BaseTool
from typing import List

def get_awsdynamodb_tools() -> List[BaseTool]:
    """Get all awsdynamodb tools."""
    from . import operations
    return operations.get_tools()

class AwsDynamodbToolkit:
    """Toolkit for interacting with awsdynamodb."""

    def __init__(self):
        """Initialize the awsdynamodb toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all awsdynamodb tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all awsdynamodb tools with default credentials."""
        return get_awsdynamodb_tools()
