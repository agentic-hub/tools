# executiondata toolkit
from langchain.tools import BaseTool
from typing import List

def get_executiondata_tools() -> List[BaseTool]:
    """Get all executiondata tools."""
    from . import operations
    return operations.get_tools()

class ExecutiondataToolkit:
    """Toolkit for interacting with executiondata."""

    def __init__(self):
        """Initialize the executiondata toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all executiondata tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all executiondata tools with default credentials."""
        return get_executiondata_tools()
