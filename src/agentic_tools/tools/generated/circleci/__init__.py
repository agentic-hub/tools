# circleci toolkit
from langchain.tools import BaseTool
from typing import List

def get_circleci_tools() -> List[BaseTool]:
    """Get all circleci tools."""
    from . import operations
    return operations.get_tools()

class CircleciToolkit:
    """Toolkit for interacting with circleci."""

    def __init__(self):
        """Initialize the circleci toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all circleci tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all circleci tools with default credentials."""
        return get_circleci_tools()
