# merge toolkit
from langchain.tools import BaseTool
from typing import List

def get_merge_tools() -> List[BaseTool]:
    """Get all merge tools."""
    from . import operations
    return operations.get_tools()

class MergeToolkit:
    """Toolkit for interacting with merge."""

    def __init__(self):
        """Initialize the merge toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all merge tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all merge tools with default credentials."""
        return get_merge_tools()
