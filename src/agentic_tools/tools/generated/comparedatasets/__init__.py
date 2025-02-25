# comparedatasets toolkit
from langchain.tools import BaseTool
from typing import List

def get_comparedatasets_tools() -> List[BaseTool]:
    """Get all comparedatasets tools."""
    from . import operations
    return operations.get_tools()

class ComparedatasetsToolkit:
    """Toolkit for interacting with comparedatasets."""

    def __init__(self):
        """Initialize the comparedatasets toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all comparedatasets tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all comparedatasets tools with default credentials."""
        return get_comparedatasets_tools()
