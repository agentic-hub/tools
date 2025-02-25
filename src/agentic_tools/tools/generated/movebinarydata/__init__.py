# movebinarydata toolkit
from langchain.tools import BaseTool
from typing import List

def get_movebinarydata_tools() -> List[BaseTool]:
    """Get all movebinarydata tools."""
    from . import operations
    return operations.get_tools()

class MovebinarydataToolkit:
    """Toolkit for interacting with movebinarydata."""

    def __init__(self):
        """Initialize the movebinarydata toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all movebinarydata tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all movebinarydata tools with default credentials."""
        return get_movebinarydata_tools()
