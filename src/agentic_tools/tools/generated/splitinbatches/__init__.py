# splitinbatches toolkit
from langchain.tools import BaseTool
from typing import List

def get_splitinbatches_tools() -> List[BaseTool]:
    """Get all splitinbatches tools."""
    from . import operations
    return operations.get_tools()

class SplitinbatchesToolkit:
    """Toolkit for interacting with splitinbatches."""

    def __init__(self):
        """Initialize the splitinbatches toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all splitinbatches tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all splitinbatches tools with default credentials."""
        return get_splitinbatches_tools()
